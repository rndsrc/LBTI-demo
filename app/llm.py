"""Claude answers a question, and the answer is streamed back as it is written."""

from __future__ import annotations

from typing import AsyncIterator

import anthropic

from app.config import Config

SYSTEM = """You are the LBTI Assistant of the Large Binocular Telescope Observatory (LBTO). You help astronomers \
who prepare or execute observations with the Large Binocular Telescope Interferometer (LBTI).

Start with the answer, no preamble. Be concise; short lists and tables are fine. Always state units."""


def thinking_for(model: str) -> dict | None:
    """No extended thinking. Claude Sonnet 5.5 rejects {"type": "disabled"}; its lowest setting is between_tools."""
    if model.startswith("claude-sonnet-5-5"):
        return {"type": "between_tools"}
    if model.startswith("claude-haiku"):
        return {"type": "disabled"}
    return None


class Chat:
    def __init__(self, cfg: Config, client: anthropic.AsyncAnthropic | None = None):
        self.cfg = cfg
        self.client = client or anthropic.AsyncAnthropic()

    async def answer(self, question: str) -> AsyncIterator[dict]:
        """Yield the answer as {"type": "text", "text": ...} events while Claude writes it."""
        request = dict(model=self.cfg.model, max_tokens=self.cfg.max_tokens, system=SYSTEM,
                       messages=[{"role": "user", "content": question}])
        if thinking := thinking_for(self.cfg.model):
            request["thinking"] = thinking
        async with self.client.messages.stream(**request) as stream:
            async for event in stream:
                if event.type == "content_block_delta" and event.delta.type == "text_delta":
                    yield {"type": "text", "text": event.delta.text}
