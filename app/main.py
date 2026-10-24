"""The web app: the chat page, a streaming chat endpoint, and a health check.

    uvicorn --factory app.main:create_app"""

from __future__ import annotations

import json
import logging

import anthropic
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.config import ROOT, Config
from app.llm import Chat
from app.search import Manual

log = logging.getLogger("lbti")


class Question(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


def sse(event: str, data: dict) -> str:
    """One server-sent event."""
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def create_app(cfg: Config | None = None, client: anthropic.AsyncAnthropic | None = None) -> FastAPI:
    cfg = cfg or Config.from_env()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    manual = Manual(cfg.index_dir)
    chat = Chat(cfg, manual, client)
    app = FastAPI(title="LBTI Assistant", docs_url=None, redoc_url=None, openapi_url=None)

    @app.get("/healthz")
    def healthz():
        return {"status": "ok", "sections": len(manual.sections), "ingested_at": manual.meta["ingested_at"]}

    @app.post("/api/chat")
    async def ask(body: Question):
        question = body.message.strip()

        async def stream():
            out: dict = {}
            try:
                async for event in chat.answer(question, out):
                    yield sse(event.pop("type"), event)
            except anthropic.APIError as e:
                log.error("Claude API error: %s", e)
                yield sse("error", {"message": "The model service returned an error. Please try again."})
                return
            log.info(json.dumps({"event": "answer", "searches": out["searches"], "question": question[:200]}))
            yield sse("done", {})

        return StreamingResponse(stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"})

    app.mount("/", StaticFiles(directory=ROOT / "web", html=True), name="web")
    return app
