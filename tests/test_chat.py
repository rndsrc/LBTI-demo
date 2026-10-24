from __future__ import annotations

import json

from fastapi.testclient import TestClient

from app.config import Config
from app.main import create_app
from tests.conftest import FakeClient, text


def events(body: str) -> list[tuple[str, dict]]:
    out = []
    for chunk in body.strip().split("\n\n"):
        event, data = chunk.split("\n")
        out.append((event.removeprefix("event: "), json.loads(data.removeprefix("data: "))))
    return out


def test_streams_the_answer():
    fake = FakeClient([([text("Hello, astronomer.")], "end_turn")])
    with TestClient(create_app(Config(), client=fake)) as client:
        ev = events(client.post("/api/chat", json={"message": "Hi"}).text)
        assert [k for k, _ in ev] == ["text", "text", "done"]
        assert "".join(d["text"] for k, d in ev if k == "text") == "Hello, astronomer."
        assert fake.calls[0]["messages"] == [{"role": "user", "content": "Hi"}]
        assert fake.calls[0]["thinking"] == {"type": "between_tools"}
        assert client.post("/api/chat", json={"message": ""}).status_code == 422
        assert client.get("/").status_code == 200
