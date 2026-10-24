"""Shared fixtures. No network: a tiny synthetic manual and a scripted fake of the streaming Claude client."""

from __future__ import annotations

import copy
from pathlib import Path
from types import SimpleNamespace

import pytest
from anthropic.types import TextBlock, Usage

from app.config import Config
from scripts.ingest import build_index, load_sections

FIXTURES = Path(__file__).parent / "fixtures"

PAGES = {
    "web/nomic-filters.md": """---
url: https://example.test/lbti/instrument-characteristics/nomic-filters/
title: NOMIC filters
breadcrumb: Instrument Characteristics › NOMIC filters
---

## Overview {#TOC-Overview}

| Filter label | Filter wheel | λc [µm] | Range [µm] |
| --- | --- | --- | --- |
| Nprime | FW1 | 11.11 | 10.22 – 12.49 |
""",
    "web/lmircam-filters.md": """---
url: https://example.test/lbti/instrument-characteristics/lmircam-filters/
title: LMIRCam Filters
breadcrumb: Instrument Characteristics › LMIRCam Filters
---

## Narrowband filters {#TOC-Narrowband-filters}

| Filter Name | Filter Wheel | λc [µm] |
| --- | --- | --- |
| Br-alpha | FW2 | 4.05 |

LMIRCam can be used together with NOMIC through the dichroic.
""",
    "pdf/LBTI_user_manual_v0.11.md": """---
url: https://example.test/LBTI_user_manual_v0.11.pdf
title: LBTI User's Manual (PDF v0.11)
breadcrumb: LBTI User's Manual PDF v0.11
---

<!-- page: 5 -->

# 4 Observing planning and execution

## 4.7 Overheads

Telescope preset 75 s; nulling alignment 1200 s.
""",
}


@pytest.fixture
def cfg(tmp_path: Path) -> Config:
    for name, text in PAGES.items():
        (tmp_path / "content" / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / "content" / name).write_text(text)
    build_index(load_sections(tmp_path / "content"), tmp_path / "index", "v0.11")
    return Config(content_dir=tmp_path / "content", index_dir=tmp_path / "index")


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
