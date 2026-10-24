"""Full-text search over the manual (index/kb.sqlite, built by scripts/ingest.py)."""

from __future__ import annotations

import json
import re
import sqlite3
from pathlib import Path

# Words that carry no search signal in questions about the manual.
STOPWORDS = set("""a an and are as at be by can could do does for from has have how i in into is it its me my of on
or should that the their them there these this to us was we were what when where which who why will with would you
your about tell explain describe give list show please lbti manual available provide information info typical
typically many much need needed get find any all some kind type types here use used using""".split())

def fts_query(text: str) -> str | None:
    """Free text -> FTS5 query: quoted terms OR-ed together, so user input is never parsed as FTS syntax."""
    words = re.findall(r"[a-z0-9]+(?:[.\-/][a-z0-9]+)*", text.lower())
    terms = list(dict.fromkeys(w for w in words if w not in STOPWORDS)) or words
    return " OR ".join(f'"{t}"' for t in terms[:32]) or None


class Manual:
    def __init__(self, index_dir: Path):
        self.db = sqlite3.connect(f"file:{index_dir / 'kb.sqlite'}?mode=ro", uri=True, check_same_thread=False)
        self.sections = {sid: {"id": sid, "source_url": url, "title": title, "paragraphs": json.loads(paras)}
                         for sid, url, title, paras in self.db.execute(
                             "SELECT id, source_url, title, paragraphs FROM sections")}
        self.meta = dict(self.db.execute("SELECT key, value FROM meta").fetchall())

    def search(self, query: str, limit: int = 6) -> list[dict]:
        """BM25 ranking; a match in a section's title counts 8 times as much as one in its text."""
        if not (q := fts_query(query)):
            return []
        rows = self.db.execute("SELECT id FROM sections WHERE sections MATCH ? "
                               "ORDER BY bm25(sections, 0, 0, 8.0, 0, 1.0) LIMIT ?", (q, limit)).fetchall()
        return [self.sections[sid] for (sid,) in rows]

