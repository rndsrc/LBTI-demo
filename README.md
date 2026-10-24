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

The whole package, tests included, is about 1,500 lines.

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

## Run it

You need an Anthropic API key and either Python 3.12 or Docker. Then open <http://localhost:8000>.

**From source:**

```bash
make venv                                   # .venv with the dependencies
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
make run                                    # index content/, then serve with auto-reload
```

**With Docker**, building the image from this checkout:

```bash
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
docker compose up -d --build
```

Or run an image someone has published:

```bash
docker run -d --env-file .env -p 8000:8000 --read-only <username>/lbti-demo
```

The image already contains the manual and its search index. It needs no volume and writes nothing to disk.
Conversations are kept in memory, so a restart forgets them.

## The knowledge base

```bash
make ingest                 # crawl the site and the PDF (1 request/s); only changed files are rewritten
git diff content/           # review what changed in the manual
make index                  # rebuild index/kb.sqlite from content/ without crawling
```

- **New PDF release:** set `PDF_URL` and `PDF_VERSION` before `make ingest`.
- **Corpus size:** `python -m scripts.ingest --offline --count-tokens` reports it with Claude's token
  counter. Today it is **83,804 tokens**, 51,463 of them in the PDF.
- **Section ids** are stable and readable, e.g. `web:lmircam-filters#narrowband-filters` or
  `pdf:p55#4-7-overheads-time-request-and-execution-time`.

## Configuration

Settings come from environment variables, or from a `.env` file (see `.env.example`). Only
`ANTHROPIC_API_KEY` is required.

| Variable | Default | Meaning |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | Claude API key (required) |
| `MODEL` | `claude-sonnet-5-5` | `claude-haiku-5-5` is much cheaper but less accurate |
| `MAX_TOKENS` | `2048` | maximum answer length |
| `MAX_SEARCHES` | `5` | searches per question before an answer is forced |
| `MAX_QUESTION_CHARS` | `2000` | longest accepted question |
| `MAX_TURNS` | `20` | questions per conversation |
| `RATE_PER_HOUR` | `30` | questions per client IP per hour |
| `PDF_URL`, `PDF_VERSION`, `MANUAL_URL` | manual v0.11 | sources for `make ingest`, shown in the banner |
| `LBTI_IMAGE`, `PORT` | `lbti-demo`, `8000` | `docker compose`: image to run, host port |
| `FORWARDED_ALLOW_IPS` | `127.0.0.1` | read by uvicorn: proxies whose `X-Forwarded-For` is trusted |

## Evaluation

`make eval` runs the 30 questions in `evals/golden.yaml` through the same code the web app uses:

- **Topics:** filters, grisms, detectors, AO, observing modes, overheads, calibrations, finding charts,
  scripts, data retrieval, astrometry and user policy.
- **Out of scope:** 3 questions the manual does not answer.
- **Web/PDF disagreements:** two questions where the web page and the PDF disagree.

It reports four measures:

- **recall@6:** an expected section is among the first search's results.
- **cites expected:** the answer cites an expected section.
- **judge mean:** a 1–5 grade from `claude-haiku-5-5`, which sees the reference answer and the cited
  passages.
- **abstentions:** the out-of-scope questions are answered "not covered".

| Run (2026-10-24) | recall@6 | cites expected | judge mean | abstentions |
|---|---:|---:|---:|---:|
| `claude-sonnet-5-5` | 1.00 | 1.00 | 4.30 | 3/3 |

Per-question results are in `evals/last_run.json`.

## Cost

A typical question takes two Claude calls: one that decides what to search, and one that reads the search
results and answers. Each call's token usage is logged as one JSON line:

```
{"event": "claude", "round": 0, "stop": "tool_use", "input_tokens": 4, "output_tokens": 128,
 "cache_creation_input_tokens": 94, "cache_read_input_tokens": 977}
{"event": "claude", "round": 1, "stop": "end_turn", "input_tokens": 2, "output_tokens": 219,
 "cache_creation_input_tokens": 13624, "cache_read_input_tokens": 1767}
```

- **Round 0:** the cached tool and system prompt are read back (977 tokens).
- **Round 1:** the search results (13.6k tokens) are written to the cache, so a follow-up question reads them
  back cheaply.

On Claude Sonnet 5.5 this comes to about 4 cents per question. To cap spending on a public demo, set a monthly
spend limit on the API key's workspace in the Claude Console; the per-IP limit only slows individual visitors
down.

## Deploying publicly

The container serves plain HTTP on port 8000. To expose it, put a TLS reverse proxy in front of it, e.g.
`caddy reverse-proxy --from lbti.example.org --to localhost:8000`, and set `FORWARDED_ALLOW_IPS` to the
proxy's address so the per-IP limit sees real clients. `docker-compose.yml` runs the container as `nobody`
with a read-only filesystem, no Linux capabilities and `no-new-privileges`.

**Publishing the image.**

- **CI:** `.github/workflows/docker.yml` runs the tests on every push and pull request. On `main` and `v*`
  tags it publishes `<DOCKERHUB_USERNAME>/lbti-demo` for amd64 and arm64, once you set the repository
  variable `DOCKERHUB_USERNAME` and the secret `DOCKERHUB_TOKEN`.
- **By hand:**

  ```bash
  docker buildx build --platform linux/amd64,linux/arm64 -t <username>/lbti-demo --push .
  ```

## Notes

- **Search instead of the whole manual.** The 84k-token corpus would fit in one prompt. Searching keeps each
  request to a few relevant sections, makes citations precise, and scales to larger document sets.
- **Plain BM25.** On this corpus it found an expected section in the first search for every answerable eval
  question, so there are no embeddings or vector database.
- **No `temperature`.** API version `2026-10-21`, which the `anthropic` 2.3 SDK uses, no longer accepts
  sampling parameters. Answers are grounded by search and citations instead.
- **Thinking off.** Extended thinking is not used. Claude Sonnet 5.5 rejects `{"type": "disabled"}`; its
  lowest setting is `{"type": "between_tools"}`.
- **PDF conversion.** `pymupdf4llm` runs in non-layout mode, because layout mode merged numbered headings
  into paragraphs on this PDF. Borderless tables come out as one row per line.
- **Pinned PDF libraries.** `pymupdf4llm`/`pymupdf` "2.0" on PyPI is an empty package, so the Artifex 1.28.2
  release is pinned.
