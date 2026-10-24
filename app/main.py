"""The web app: the chat page, a streaming chat endpoint, and a health check.

    uvicorn --factory app.main:create_app

Conversations live in memory (a restart forgets them); the app writes nothing to disk."""

from __future__ import annotations

import json
import logging
import secrets
import time
from collections import OrderedDict, defaultdict, deque

import anthropic
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.config import ROOT, Config
from app.llm import Chat
from app.search import Manual

log = logging.getLogger("lbti")
MAX_CONVERSATIONS = 1000
SECURITY_HEADERS = {
    "Content-Security-Policy": "default-src 'self'; img-src 'self' data:; frame-ancestors 'none'; base-uri 'self'",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


class Question(BaseModel):
    message: str = Field(min_length=1, max_length=20_000)
    conversation_id: str | None = Field(default=None, max_length=64)


def sse(event: str, data: dict) -> str:
    """One server-sent event."""
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def create_app(cfg: Config | None = None, client: anthropic.AsyncAnthropic | None = None) -> FastAPI:
    cfg = cfg or Config.from_env()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    manual = Manual(cfg.index_dir)
    chat = Chat(cfg, manual, client)
    conversations: OrderedDict[str, tuple[int, list]] = OrderedDict()  # id -> (turns, messages), oldest first
    recent: defaultdict[str, deque] = defaultdict(deque)                # client IP -> times of recent questions

    app = FastAPI(title="LBTI Assistant", docs_url=None, redoc_url=None, openapi_url=None)

    @app.middleware("http")
    async def security_headers(request: Request, call_next):
        response = await call_next(request)
        response.headers.update(SECURITY_HEADERS)
        return response

    @app.get("/api/info")
    def info():
        return {"pdf_version": manual.meta["pdf_version"], "ingested_at": manual.meta["ingested_at"][:10],
                "manual_url": cfg.manual_url, "max_chars": cfg.max_question_chars}

    @app.get("/healthz")
    def healthz():
        return {"status": "ok", "sections": len(manual.sections), "ingested_at": manual.meta["ingested_at"]}

    @app.post("/api/chat")
    async def ask(body: Question, request: Request):
        question = body.message.strip()
        if not question or len(question) > cfg.max_question_chars:
            raise HTTPException(413, f"Questions are limited to {cfg.max_question_chars} characters.")
        now, times = time.time(), recent[request.client.host if request.client else "?"]
        while times and times[0] < now - 3600:
            times.popleft()
        if len(times) >= cfg.rate_per_hour:
            raise HTTPException(429, f"Limit of {cfg.rate_per_hour} questions per hour reached. Try again later.")
        times.append(now)
        cid = body.conversation_id if body.conversation_id in conversations else secrets.token_urlsafe(12)
        turns, history = conversations.get(cid, (0, []))
        if turns >= cfg.max_turns:
            raise HTTPException(409, "This conversation is long enough; please start a new chat.")

        async def stream():
            out: dict = {}
            yield sse("meta", {"conversation_id": cid})
            try:
                async for event in chat.answer(history, question, out):
                    yield sse(event.pop("type"), event)
            except anthropic.APIError as e:
                log.error("Claude API error: %s", e)
                yield sse("error", {"message": "The model service returned an error. Please try again."})
                return
            if not out.get("refused"):
                conversations[cid] = (turns + 1, out["messages"])
                conversations.move_to_end(cid)
                while len(conversations) > MAX_CONVERSATIONS:
                    conversations.popitem(last=False)
            log.info(json.dumps({"event": "answer", "conversation": cid, "searches": out["searches"],
                                 "sources": len(out["sources"]), "question": question[:200]}))
            yield sse("done", {})

        return StreamingResponse(stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"})

    app.mount("/", StaticFiles(directory=ROOT / "web", html=True), name="web")
    return app
