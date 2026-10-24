"""Build the knowledge base: crawl the LBTI User's Manual (web pages + PDF), convert it to Markdown, split it
into citable sections, and index them for full-text search with SQLite FTS5.

    python -m scripts.ingest                  # crawl the live site and PDF, then rebuild the index
    python -m scripts.ingest --offline        # rebuild the index from the committed content/ (Docker build)
    python -m scripts.ingest --count-tokens   # also report corpus size with the Claude token counter

content/ is committed to git so changes to the manual show up as diffs. Files are rewritten only when
their content changes.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import json
import re
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin, urlparse

import yaml
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

from app.config import Config

SITE_ROOT = "https://scienceops.lbto.org/lbti/"
WEB_URLS = [SITE_ROOT + path + "/" for path in """
    lbti-home lbti-user-policy lbti-users-manual optical-path nic ao-wfs
    instrument-characteristics instrument-characteristics/lmircam-filters
    instrument-characteristics/lmircam-prism-grisms-other instrument-characteristics/nomic-filters
    instrument-characteristics/detectors planning-observations planning-observations/modes-and-strategies
    planning-observations/modes-and-strategies/ao-imaging planning-observations/modes-and-strategies/nales
    planning-observations/modes-and-strategies/nulling planning-observations/near-thermal-ir-observing
    planning-observations/readme planning-observations/finding-charts planning-observations/overheads
    planning-observations/calibrations observing observing/software-scripts data-retrieval-reduction-publication
    data-retrieval-reduction-publication/distortion-correction-and-astrometric-solution
    data-retrieval-reduction-publication/documents-and-links""".split()]
USER_AGENT = "LBTI-Assistant-ingest/1.0 (+https://scienceops.lbto.org/lbti/; polite crawler, 1 req/s)"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def slug_for(url: str) -> str:
    return urlparse(url).path.rstrip("/").split("/")[-1]


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s.-]", "", text.lower()).replace("_", " ")
    text = re.sub(r"[\s.]+", "-", text.strip())
    return re.sub(r"-{2,}", "-", text).strip("-") or "section"


# --------------------------------------------------------------------------------------------------
# Markdown files with YAML frontmatter
# --------------------------------------------------------------------------------------------------

def read_doc(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        _, front, body = text.split("---\n", 2)
        return yaml.safe_load(front) or {}, body.lstrip("\n")
    return {}, text


def write_doc(path: Path, meta: dict, body: str) -> bool:
    """Write frontmatter + body unless the body's hash is unchanged. Returns True if written."""
    meta = {**meta, "sha256": hashlib.sha256(body.encode()).hexdigest()}
    if path.exists() and read_doc(path)[0].get("sha256") == meta["sha256"]:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=1000)
    path.write_text(f"---\n{front}---\n\n{body.strip()}\n", encoding="utf-8")
    return True


# --------------------------------------------------------------------------------------------------
# Web pages -> Markdown
# --------------------------------------------------------------------------------------------------

class _Converter(MarkdownConverter):
    def convert_img(self, el, text, parent_tags):  # keep every image as a Markdown image line
        alt = (el.get("alt") or "").strip().replace("[", "(").replace("]", ")").replace("\n", " ")
        src = el.get("src") or ""
        return f"![{alt}]({src})" if src else alt


def _expand_table_spans(table: Tag) -> None:
    """Replace rowspan/colspan with duplicated cells so the Markdown table keeps its columns."""
    def span(cell: Tag, attr: str) -> int:
        v = str(cell.attrs.pop(attr, "1")).strip()
        return min(int(v), 50) if v.isdigit() and int(v) > 0 else 1

    occupied: dict[tuple[int, int], Tag] = {}
    for r, tr in enumerate(tr for tr in table.find_all("tr") if tr.find_parent("table") is table):
        out: list[Tag] = []
        c = 0
        for cell in tr.find_all(["td", "th"], recursive=False):
            while (r, c) in occupied:
                out.append(copy.copy(occupied.pop((r, c))))
                c += 1
            rs, cs = span(cell, "rowspan"), span(cell, "colspan")
            for dc in range(cs):
                out.append(cell if dc == 0 else copy.copy(cell))
                for dr in range(1, rs):
                    occupied[(r + dr, c + dc)] = cell
            c += cs
        while (r, c) in occupied:
            out.append(copy.copy(occupied.pop((r, c))))
            c += 1
        for child in list(tr.children):
            child.extract()
        for cell in out:
            tr.append(cell)


def extract_main(html: str, url: str) -> tuple[str, str]:
    """(title, markdown) of a page's article column, without site navigation, sidebar or footer."""
    soup = BeautifulSoup(html, "html.parser")
    main = soup.select_one(".content-left") or soup.select_one("main") or soup.body
    h1 = main.find("h1") or soup.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else slug_for(url)
    if h1 is not None and h1 in main.descendants:
        h1.decompose()
    for sel in ["script", "style", "noscript", "form", "nav", "iframe", "button", "input", "footer", "header",
                ".sites-embed-type-toc", ".goog-toc", ".widget", ".sidebar", ".search-form", ".screen-reader-text",
                "#sites-page-title-header", ".sites-page-title"]:
        for el in main.select(sel):
            el.decompose()

    # Google-Sites layout tables wrap whole pages: unwrap any table that contains headings or tables.
    while (layout := next((t for t in main.find_all("table") if t.find(["h1", "h2", "h3", "h4", "table"])
                           or "sites-layout" in " ".join(t.get("class", []))), None)):
        box = soup.new_tag("div")
        for cell in layout.find_all(["td", "th"]):
            if cell.find_parent("table") is layout:
                inner = soup.new_tag("div")
                for child in list(cell.contents):
                    inner.append(child.extract())
                box.append(inner)
        layout.replace_with(box)

    for a in main.find_all("a", href=True):
        if a["href"].strip().lower().startswith("javascript:"):
            a.unwrap()
        else:
            a["href"] = urljoin(url, a["href"].strip())
    for img in main.find_all("img"):
        if img.get("src") or img.get("data-src"):
            img["src"] = urljoin(url, img.get("src") or img.get("data-src"))
        fig = img.find_parent("figure")
        if fig and fig.find("figcaption") and not img.get("alt"):
            img["alt"] = fig.find("figcaption").get_text(" ", strip=True)

    # Headings keep the page's own anchor as a {#anchor} suffix, so citations can deep-link.
    used: set[str] = set()
    for h in main.find_all(["h2", "h3", "h4", "h5", "h6"]):
        text = h.get_text(" ", strip=True).replace("\xa0", " ").strip()
        if not text:
            h.decompose()
            continue
        anchor = h.get("id")
        for a in h.find_all("a"):
            anchor = anchor or a.get("name") or a.get("id")
            if not a.get("href"):
                a.unwrap()
        if h.name in ("h2", "h3"):
            anchor = base = anchor or slugify(text)
            n = 2
            while anchor in used:
                anchor, n = f"{base}-{n}", n + 1
            used.add(anchor)
            h.clear()
            h.append(NavigableString(f"{text} {{#{anchor}}}"))

    for table in main.find_all("table"):
        _expand_table_spans(table)
    md = _Converter(heading_style="ATX", bullets="-", table_infer_header=True, escape_underscores=False,
                    escape_asterisks=False, strip=["span", "font"]).convert_soup(main)
    md = re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+\n", "\n", md.replace("\xa0", " ")))
    return title, re.sub(r"\\\{#([^}\\]+)\\?\}", r"{#\1}", md).strip()


def breadcrumbs(titles: dict[str, str]) -> dict[str, str]:
    """'Instrument Characteristics › LMIRCam Filters': the site's navigation tree mirrors the URL path."""
    crumbs = {}
    for url in titles:
        parts = urlparse(url).path.strip("/").split("/")[1:]
        crumbs[url] = " › ".join(titles.get(SITE_ROOT + "/".join(parts[:i]) + "/", parts[i - 1].replace("-", " ").title())
                                 for i in range(1, len(parts) + 1))
    return crumbs


def crawl_web(cfg: Config, client) -> list[str]:
    """Fetch WEB_URLS at 1 request/s into content/web/<slug>.md. Returns the URLs whose content changed."""
    pages = {}
    for url in WEB_URLS:
        time.sleep(1.0)
        try:
            r = client.get(url)
            r.raise_for_status()
            pages[url] = extract_main(r.text, url)
        except Exception as e:  # keep the committed copy of a page that fails
            print(f"warning: {url}: {e}")
    crumbs = breadcrumbs({u: title for u, (title, _) in pages.items()})
    return [url for url, (title, md) in pages.items()
            if write_doc(cfg.content_dir / "web" / f"{slug_for(url)}.md",
                         {"url": url, "title": title, "breadcrumb": crumbs[url], "fetched_at": now_iso()}, md)]


# --------------------------------------------------------------------------------------------------
# PDF -> Markdown
# --------------------------------------------------------------------------------------------------

def _clean_pdf_text(line: str) -> str:
    """Undo pymupdf4llm styling artefacts that hurt search and citations."""
    line = re.sub(r"</?u>", "", line)
    line = re.sub(r"~~(\w{1,2})~~\s?", r"\1", line)        # "Full ~~I~~ mage" -> "Full Image"
    line = re.sub(r"\*\*\s+\*\*", " ", line)              # "**Table** **3.4:**" -> "**Table 3.4:**"
    line = re.sub(r"\*\*\*\*", "", line)
    line = re.sub(r"\s?_([^\w\s_])_\s?", lambda m: {".": ".", ",": ", "}.get(m.group(1), f" {m.group(1)} "), line)
    line = re.sub(r"(\d)\s\.\s?(\d)", r"\1.\2", line)     # "55 . 0 ms" -> "55.0 ms"
    return re.sub(r"[ \t]{2,}", " ", line)


def clean_pdf_pages(pages: list[str]) -> str:
    """Join pages with <!-- page: N --> markers, drop running headers and page numbers, and set heading
    levels from the numbering: chapter "N" -> '#', "N.M" -> '##', "N.M.K" -> '###', unnumbered -> '##'."""
    out = []
    for n, raw in enumerate(pages, start=1):
        lines = raw.splitlines()
        idx = [i for i, line in enumerate(lines) if line.strip()]
        if idx and re.fullmatch(r"(_[^_\n]+_\s*)+", lines[idx[0]].strip()):
            lines[idx[0]] = ""
        if idx and re.fullmatch(r"[ivxlc\d]+", lines[idx[-1]].strip(), re.I):
            lines[idx[-1]] = ""
        fixed = []
        for line in lines:
            if not line.startswith("#"):
                fixed.append(_clean_pdf_text(line.rstrip()))
                continue
            text = re.sub(r"\s+", " ", re.sub(r"</?u>|\*\*|__", "", line.lstrip("#"))).strip()
            if m := re.match(r"(\d+(?:\.\d+)*)\s+\S", text):
                fixed.append("#" * min(m.group(1).count(".") + 1, 3) + " " + text)
            elif text.lower().startswith("version") or n == 1:
                fixed.append("# " + text if text.lower() == "lbti user manual" else text)
            else:
                fixed.append("## " + text)
        out.append(f"<!-- page: {n} -->\n\n" + re.sub(r"\n{3,}", "\n\n", "\n".join(fixed)).strip())
    return "\n\n".join(out) + "\n"


def fetch_pdf(cfg: Config, client) -> bool:
    import pymupdf
    import pymupdf4llm

    r = client.get(cfg.pdf_url, timeout=120)
    r.raise_for_status()
    path = cfg.content_dir / "pdf" / f"LBTI_user_manual_{cfg.pdf_version}.md"
    digest = hashlib.sha256(r.content).hexdigest()
    if path.exists() and read_doc(path)[0].get("source_sha256") == digest:
        return False
    # Non-layout mode: layout mode merged numbered headings into paragraphs on this manual.
    pymupdf4llm.use_layout(False)
    chunks = pymupdf4llm.to_markdown(pymupdf.open(stream=r.content, filetype="pdf"), page_chunks=True,
                                     table_strategy="lines_strict", show_progress=False)
    for old in path.parent.glob("LBTI_user_manual_*.md"):  # index only the configured version
        old.unlink()
    meta = {"url": cfg.pdf_url, "title": f"LBTI User's Manual (PDF {cfg.pdf_version})",
            "breadcrumb": f"LBTI User's Manual PDF {cfg.pdf_version}", "version": cfg.pdf_version,
            "fetched_at": now_iso(), "source_sha256": digest}
    return write_doc(path, meta, clean_pdf_pages([c["text"] for c in chunks]))


# --------------------------------------------------------------------------------------------------
# Sections
# --------------------------------------------------------------------------------------------------

@dataclass
class Section:
    id: str                 # web:<slug>#<heading-slug> or pdf:p<page>#<heading-slug>
    source_url: str         # page URL + #anchor, or PDF URL + #page=N
    title: str              # breadcrumb › heading
    paragraphs: list[str]   # citation units: one per paragraph, table or list


_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*(?:\{#([^}]+)\})?\s*$")
_PAGE = re.compile(r"^<!-- page: (\d+) -->$")
_LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


def paragraphs_of(body: str) -> list[str]:
    """One block per paragraph, table or list; minor headings (H4+) are attached to the block below them."""
    blocks: list[str] = []
    heading = ""
    for chunk in re.split(r"\n\s*\n", body):
        chunk = "\n".join(line for line in chunk.splitlines() if not _PAGE.match(line.strip())).strip()
        if not chunk:
            continue
        if re.fullmatch(r"#{1,6} [^\n]*", chunk):
            heading = f"{heading}\n{chunk}" if heading else chunk
            continue
        if heading:
            chunk, heading = f"{heading}\n{chunk}", ""
        if blocks and _LIST_ITEM.match(chunk) and _LIST_ITEM.match(blocks[-1].splitlines()[-1]):
            blocks[-1] += "\n" + chunk
        else:
            blocks.append(chunk)
    return blocks + [heading] if heading else blocks


def split_sections(meta: dict, body: str, origin: str, doc: str) -> list[Section]:
    """Sections on H2/H3 (and H1 chapters in the PDF). Text before the first heading is the page intro."""
    levels = {1, 2, 3} if origin == "pdf" else {2, 3}
    crumb = meta.get("breadcrumb") or meta.get("title") or doc
    cur = {"heading": meta.get("title", doc), "anchor": None, "page": 1, "parents": [], "lines": []}
    raw, stack, page = [cur], {}, 1
    for line in body.splitlines():
        if m := _PAGE.match(line.strip()):
            page = int(m.group(1))
        elif (m := _HEADING.match(line)) and len(m.group(1)) in levels:
            level = len(m.group(1))
            stack = {k: v for k, v in stack.items() if k < level}
            cur = {"heading": m.group(2).strip(), "anchor": m.group(3), "page": page,
                   "parents": [stack[k] for k in sorted(stack)], "lines": []}
            stack[level] = cur["heading"]
            raw.append(cur)
            continue
        cur["lines"].append(line)

    sections, used = [], set()
    for r in raw:
        paras = paragraphs_of("\n".join(r["lines"]))
        if not paras or (origin == "pdf" and r["heading"].lower() == "contents") \
                or " ".join(paras).strip().lower() == "contents":
            continue
        base = f"web:{doc}#{slugify(r['heading'])}" if origin == "web" else f"pdf:p{r['page']}#{slugify(r['heading'])}"
        sid, n = base, 2
        while sid in used:
            sid, n = f"{base}-{n}", n + 1
        used.add(sid)
        if origin == "web":
            url = f"{meta['url']}#{r['anchor']}" if r["anchor"] else meta["url"]
        else:
            url = f"{meta['url']}#page={r['page']}"
        path = [crumb] if r["heading"] == meta.get("title") else [crumb, *r["parents"], r["heading"]]
        sections.append(Section(sid, url, " › ".join(dict.fromkeys(path)), paras))
    return sections


def load_sections(content_dir: Path) -> list[Section]:
    order = {slug_for(u): i for i, u in enumerate(WEB_URLS)}
    sections = []
    for origin in ("web", "pdf"):
        for path in sorted((content_dir / origin).glob("*.md"), key=lambda p: (order.get(p.stem, 999), p.stem)):
            meta, body = read_doc(path)
            sections += split_sections(meta, body, origin, path.stem)
    return sections


# --------------------------------------------------------------------------------------------------
# Index
# --------------------------------------------------------------------------------------------------

def build_index(sections: list[Section], index_dir: Path, pdf_version: str) -> None:
    """Write index/kb.sqlite: one FTS5 table of sections (title and text are searchable) and a meta table.
    The new file replaces the old one only when complete."""
    index_dir.mkdir(parents=True, exist_ok=True)
    tmp = index_dir / "kb.sqlite.tmp"
    tmp.unlink(missing_ok=True)
    con = sqlite3.connect(tmp)
    con.executescript("""
        CREATE VIRTUAL TABLE sections USING fts5(id UNINDEXED, source_url UNINDEXED, title, paragraphs UNINDEXED,
                                                 text, tokenize='porter unicode61');
        CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);""")
    con.executemany("INSERT INTO sections VALUES (?, ?, ?, ?, ?)",
                    [(s.id, s.source_url, s.title, json.dumps(s.paragraphs, ensure_ascii=False),
                      "\n\n".join(s.paragraphs)) for s in sections])
    con.executemany("INSERT INTO meta VALUES (?, ?)", [("ingested_at", now_iso()), ("pdf_version", pdf_version)])
    con.commit()
    con.close()
    tmp.replace(index_dir / "kb.sqlite")


def count_tokens(cfg: Config) -> None:
    import anthropic

    client = anthropic.Anthropic()
    total = 0
    for path in sorted(cfg.content_dir.glob("*/*.md")):
        n = client.messages.count_tokens(model=cfg.model, messages=[{"role": "user", "content": read_doc(path)[1]}])
        total += n.input_tokens
        print(f"{n.input_tokens:>8,}  {path.stem}")
    print(f"{total:>8,}  total ({cfg.model})")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--offline", action="store_true", help="index the committed content/ without crawling")
    ap.add_argument("--count-tokens", action="store_true", help="report token counts (needs ANTHROPIC_API_KEY)")
    args = ap.parse_args()
    cfg = Config.from_env()
    if not args.offline:
        import httpx

        with httpx.Client(headers={"User-Agent": USER_AGENT}, timeout=30, follow_redirects=True) as client:
            changed = crawl_web(cfg, client)
            if fetch_pdf(cfg, client):
                changed.append(cfg.pdf_url)
        print("changed:", *changed or ["nothing"], sep="\n  ")
    sections = load_sections(cfg.content_dir)
    build_index(sections, cfg.index_dir, cfg.pdf_version)
    print(f"indexed {len(sections)} sections into {cfg.index_dir / 'kb.sqlite'}")
    if args.count_tokens:
        count_tokens(cfg)


if __name__ == "__main__":
    main()
