"""Fetch the LBTI User's Manual web pages and convert them to Markdown in content/web/.

    python -m scripts.ingest

content/ is committed to git so changes to the manual show up as diffs. Files are rewritten only when
their content changes.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import re
import time
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
# Entry point
# --------------------------------------------------------------------------------------------------

def main() -> None:
    argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter).parse_args()
    cfg = Config.from_env()
    import httpx

    with httpx.Client(headers={"User-Agent": USER_AGENT}, timeout=30, follow_redirects=True) as client:
        changed = crawl_web(cfg, client)
    print("changed:", *changed or ["nothing"], sep="\n  ")


if __name__ == "__main__":
    main()
