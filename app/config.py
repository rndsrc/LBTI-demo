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
    content_dir: Path = ROOT / "content"

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
