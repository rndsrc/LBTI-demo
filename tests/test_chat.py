from __future__ import annotations

import json

from fastapi.testclient import TestClient

from app.main import create_app
from tests.conftest import FakeClient, text, tool


def events(body: str) -> list[tuple[str, dict]]:
    out = []
    for chunk in body.strip().split("\n\n"):
        event, data = chunk.split("\n")
        out.append((event.removeprefix("event: "), json.loads(data.removeprefix("data: "))))
    return out


def test_search_round_then_answer(cfg):
    fake = FakeClient([
        ([text("Let me search."), tool("t1", "search_manual", {"query": "Br-alpha filter"})], "tool_use"),
        ([text("Br-alpha is in FW2 at 4.05 µm.")], "end_turn"),
    ])
    with TestClient(create_app(cfg, client=fake)) as client:
        ev = events(client.post("/api/chat", json={"message": "Where is Br-alpha?"}).text)
        kinds = [k for k, _ in ev]
        assert [k for k in kinds if k != "text"] == ["status", "retract", "done"]
        assert dict(ev)["status"]["text"] == "Searching the manual for “Br-alpha filter”…"
        # the narration before the search is retracted; only the answer remains
        answer = ev[kinds.index("retract") + 1:]
        assert "".join(d["text"] for k, d in answer if k == "text") == "Br-alpha is in FW2 at 4.05 µm."

        first, second = fake.calls
        assert first["tools"][0]["name"] == "search_manual" and "LBTI User's Manual" in first["system"]
        [result] = second["messages"][-1]["content"]
        assert result["tool_use_id"] == "t1" and "Br-alpha" in result["content"][0]["text"]


def test_page_and_health(cfg):
    with TestClient(create_app(cfg, client=FakeClient([]))) as client:
        assert client.get("/").status_code == 200
        assert client.get("/healthz").json()["sections"] == 3
