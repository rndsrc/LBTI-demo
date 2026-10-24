"""Shared fixtures. No network: saved manual pages and a scripted fake of the streaming Claude client."""

from __future__ import annotations

import copy
from pathlib import Path
from types import SimpleNamespace

from anthropic.types import TextBlock, Usage

FIXTURES = Path(__file__).parent / "fixtures"

def text(t: str, cites: list[dict] | None = None) -> TextBlock:
    return TextBlock.model_construct(type="text", text=t, citations=cites)


class FakeClient:
    """Replays scripted responses as stream events; records the requests it received."""

    def __init__(self, turns: list[tuple[list, str]]):
        self.turns, self.calls = list(turns), []
        self.messages = self

    def stream(self, **request):
        self.calls.append(copy.deepcopy(request))
        blocks, stop = self.turns.pop(0)
        return FakeStream(blocks, stop)


class FakeStream:
    def __init__(self, blocks: list, stop: str):
        self.blocks, self.stop = blocks, stop

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        return False

    async def __aiter__(self):
        ev = SimpleNamespace
        for i, b in enumerate(self.blocks):
            yield ev(type="content_block_start", index=i, content_block=b)
            if b.type == "text":
                for c in b.citations or []:
                    c = ev(**(c if isinstance(c, dict) else c.to_dict()))
                    yield ev(type="content_block_delta", index=i, delta=ev(type="citations_delta", citation=c))
                for half in (b.text[: len(b.text) // 2], b.text[len(b.text) // 2:]):
                    yield ev(type="content_block_delta", index=i, delta=ev(type="text_delta", text=half))
            yield ev(type="content_block_stop", index=i, content_block=b)

    async def get_final_message(self):
        return SimpleNamespace(content=self.blocks, stop_reason=self.stop,
                               usage=Usage.model_construct(input_tokens=10, output_tokens=5,
                                                           cache_creation_input_tokens=0, cache_read_input_tokens=900))
