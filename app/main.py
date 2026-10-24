"""The web app: the chat page and a streaming chat endpoint.

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

log = logging.getLogger("lbti")


class Question(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


def sse(event: str, data: dict) -> str:
    """One server-sent event."""
    return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def create_app(cfg: Config | None = None, client: anthropic.AsyncAnthropic | None = None) -> FastAPI:
    cfg = cfg or Config.from_env()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    chat = Chat(cfg, client)
    app = FastAPI(title="LBTI Assistant", docs_url=None, redoc_url=None, openapi_url=None)

    @app.post("/api/chat")
    async def ask(body: Question):
        question = body.message.strip()

        async def stream():
            try:
                async for event in chat.answer(question):
                    yield sse(event.pop("type"), event)
            except anthropic.APIError as e:
                log.error("Claude API error: %s", e)
                yield sse("error", {"message": "The model service returned an error. Please try again."})
                return
            yield sse("done", {})

        return StreamingResponse(stream(), media_type="text/event-stream", headers={"Cache-Control": "no-cache"})

    app.mount("/", StaticFiles(directory=ROOT / "web", html=True), name="web")
    return app
