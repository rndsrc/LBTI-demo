# LBTI Assistant

A small chatbot that answers astronomers' questions about the Large Binocular Telescope Interferometer (LBTI)
from the **LBTI User's Manual** of the Large Binocular Telescope Observatory (LBTO). Claude searches the
manual through a tool and cites the exact paragraph each claim comes from. Each citation appears as a numbered
chip that links to the web page or PDF page and shows the quoted passage.

It is meant as a readable example of how to serve a document collection with an LLM:

- turn a website and a PDF into citable sections;
- let the model search them instead of reading everything;
- keep the shared prompt cached;
- stream grounded answers;
- measure quality with a small eval.

## Design

```
 scripts/ingest.py                         (run once, or when the manual changes)
   26 manual web pages ──► HTML → Markdown ──┐
   PDF manual v0.11    ──► PDF → Markdown  ──┴─► content/*.md ──► sections ──► index/kb.sqlite (FTS5)
                                               (kept in git)    (H2/H3 headings)

 app/                                      (the running service)
   browser ──POST /api/chat──► main.py ──► llm.py ──stream──► Claude API
      ▲                                     │  tool: search_manual
      └──── server-sent events ◄────────────┘   └─► search.py: BM25 over kb.sqlite
            answer text with [n] markers, sources
```

- **Knowledge base** (`scripts/ingest.py`):
  - The manual's 26 web pages and its PDF are converted to Markdown and committed to `content/`, so a
    change to the manual shows up as a git diff.
  - Each document is split into sections at its headings. Within a section, every paragraph, table and
    list is a separate *citation unit*.
  - The sections are indexed with SQLite's FTS5 full-text search.
- **Search** (`app/search.py`):
  - BM25 ranking, with a match in a section's title counting eight times as much as one in its text.
  - Claude reaches it through one tool, `search_manual(query)`.
  - Each hit goes back as a `search_result` block with citations enabled, one text block per citation unit.
- **Answering** (`app/llm.py`):
  - Every request is *tool + system prompt + conversation*.
  - The system prompt holds the grounding rules: answer only from what the search returned, quote numbers
    exactly, say when the manual does not cover something, and prefer the web pages over the older PDF.
  - Claude searches as often as it needs (up to five times), then streams the answer.
  - Citations turn into `[n]` markers after the cited text, plus a numbered list of sources.
- **Prompt caching:** the tool and the system prompt are the same for every user, so they are cached for an
  hour. Each growing conversation is cached too, so follow-up questions reuse what was already read.
- **Web app** (`app/main.py`, `web/`):
  - FastAPI streams events to a single static page. The page renders Markdown with the vendored `marked`,
    sanitizes it with `DOMPurify`, and turns the markers into citation chips.
  - Conversations stay in memory, and a per-IP hourly limit protects the API key.
- **Evaluation** (`scripts/eval.py`): 30 questions written from the manual, graded for retrieval, citations,
  correctness and declining questions the manual does not answer.

| File | What it does |
|---|---|
| `scripts/ingest.py` | crawl, convert, split into sections, index |
| `app/search.py` | full-text search and the `search_manual` tool |
| `app/llm.py` | system prompt, tool loop, caching, citations |
| `app/main.py` | web app and streaming endpoint |
| `app/config.py` | settings from the environment |
| `web/` | chat page (HTML, JavaScript, CSS) |
| `scripts/eval.py` | golden-question evaluation |
| `tests/` | ingest, search and chat tests, with a fake Claude client |
