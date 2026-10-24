"""Settings, read once from environment variables (or a .env file in the working directory)."""

from __future__ import annotations

import os
from dataclasses import dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Config:
    model: str = "claude-sonnet-5-5"   # ANTHROPIC_API_KEY is read by the anthropic SDK itself
    max_tokens: int = 2048             # per answer
    max_searches: int = 5              # per question, before an answer is forced
    max_question_chars: int = 2000
    max_turns: int = 20                # questions per conversation
    rate_per_hour: int = 30            # questions per client IP, to protect the API key on a public demo
    content_dir: Path = ROOT / "content"
    index_dir: Path = ROOT / "index"
    pdf_url: str = "https://scienceops.lbto.org/wp-content/uploads/2024/05/LBTI_user_manual_v0.11.pdf"
    pdf_version: str = "v0.11"

    @classmethod
    def from_env(cls) -> Config:
        """Each field can be set by the upper-case environment variable of the same name, e.g. MAX_TOKENS."""
        dotenv = Path(".env")
        if dotenv.is_file():  # KEY=VALUE lines; real environment variables win
            for line in dotenv.read_text().splitlines():
                key, sep, value = line.partition("=")
                if sep and not key.lstrip().startswith("#"):
                    os.environ.setdefault(key.strip(), value.strip())
        return cls(**{f.name: type(f.default)(os.environ[f.name.upper()]) for f in fields(cls)
                      if os.environ.get(f.name.upper())})
