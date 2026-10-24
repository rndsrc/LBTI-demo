from __future__ import annotations

import json

from fastapi.testclient import TestClient

from app.main import create_app
from tests.conftest import FakeClient, text, tool

SRC = "https://example.test/lbti/instrument-characteristics/lmircam-filters/#TOC-Narrowband-filters"
TITLE = "Instrument Characteristics › LMIRCam Filters › Narrowband filters"


def cite(passage: str) -> dict:
    return {"type": "search_result_location", "source": SRC, "title": TITLE, "cited_text": passage}


def events(body: str) -> list[tuple[str, dict]]:
    out = []
    for chunk in body.strip().split("\n\n"):
        event, data = chunk.split("\n")
        out.append((event.removeprefix("event: "), json.loads(data.removeprefix("data: "))))
    return out


def test_search_round_then_cited_answer_then_follow_up(cfg):
    fake = FakeClient([
        ([text("Let me search."), tool("t1", "search_manual", {"query": "Br-alpha filter"})], "tool_use"),
        ([text("Br-alpha is in FW2", [cite("| Br-alpha | FW2 | 4.05 |")]),
          text(" at 4.05 µm.\n", [cite("| Br-alpha | FW2 | 4.05 |")])], "end_turn"),
        ([text("It can be combined with NOMIC.", [cite("LMIRCam can be used together with NOMIC.")])], "end_turn"),
    ])
    with TestClient(create_app(cfg, client=fake)) as client:
        ev = events(client.post("/api/chat", json={"message": "Where is Br-alpha?"}).text)
        kinds = [k for k, _ in ev]
        assert [k for k in kinds if k != "text"] == ["meta", "status", "retract", "sources", "done"]
        assert dict(ev)["status"]["text"] == "Searching the manual for “Br-alpha filter”…"
        # after the retract, the marker follows the cited text and is shown once per line
        answer = ev[kinds.index("retract") + 1:]
        assert "".join(d["text"] for k, d in answer if k == "text") == "Br-alpha is in FW2[1] at 4.05 µm.\n"
        assert ev[-2][1]["sources"] == [{"n": 1, "source": SRC, "title": TITLE, "cited_text": ["| Br-alpha | FW2 | 4.05 |"]}]

        first, second = fake.calls[:2]
        assert first["system"][0]["cache_control"] == first["tools"][0]["cache_control"] == {"type": "ephemeral",
                                                                                           "ttl": "1h"}
        assert first["cache_control"] == {"type": "ephemeral"} and first["thinking"] == {"type": "between_tools"}
        [result] = second["messages"][-1]["content"]
        assert result["tool_use_id"] == "t1" and result["content"][0]["type"] == "search_result"

        cid = ev[0][1]["conversation_id"]
        follow = events(client.post("/api/chat", json={"message": "And NOMIC?", "conversation_id": cid}).text)
        assert follow[0][1]["conversation_id"] == cid
        third = fake.calls[2]["messages"]
        assert third[:3] == second["messages"] and third[3]["role"] == "assistant"
        assert third[4] == {"role": "user", "content": "And NOMIC?"}


def test_limits(cfg):
    fake = FakeClient([([text("ok")], "end_turn")] * 5)
    with TestClient(create_app(cfg, client=fake)) as client:
        assert client.post("/api/chat", json={"message": "x" * 2001}).status_code == 413
        assert client.post("/api/chat", json={"message": ""}).status_code == 422
        for _ in range(5):
            assert client.post("/api/chat", json={"message": "hi"}).status_code == 200
        assert client.post("/api/chat", json={"message": "hi"}).status_code == 429  # 5 per hour in this config


def test_page_and_health(cfg):
    with TestClient(create_app(cfg, client=FakeClient([]))) as client:
        page = client.get("/")
        assert page.status_code == 200 and "default-src 'self'" in page.headers["content-security-policy"]
        assert client.get("/healthz").json()["sections"] == 3
