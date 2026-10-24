from __future__ import annotations

from scripts.ingest import WEB_URLS, breadcrumbs, clean_pdf_pages, extract_main, paragraphs_of, split_sections
from tests.conftest import FIXTURES

URL = "https://scienceops.lbto.org/lbti/instrument-characteristics/lmircam-filters/"


def test_extract_main_content_only():
    title, md = extract_main((FIXTURES / "lmircam-filters.html").read_text(), URL)
    assert title == "LMIRCam Filters"
    # headings keep the page's own anchors
    assert "## Overview {#TOC-Overview}" in md
    assert "### Narrowband filters {#TOC-Narrowband-filters}" in md
    # tables survive as Markdown tables, one row per line
    assert "| Filter Name | Filter Wheel & Pos | λc [µm] | Range  [µm] | Comments |" in md
    assert "| StdL | FW4 | 3.70 | 3.41 – 3.99 | Optimized for planets |" in md
    # rowspan cells are duplicated into every row they cover
    assert md.count("use PK50 in FW4, so as to prevent L-band light leakage") >= 3
    # site chrome is gone: sidebar navigation, footer, embedded TOC widget
    assert "Navigation" not in md
    assert "Get Connected" not in md
    assert "Contents" not in md.splitlines()[0]
    # images become Markdown image lines with absolute URLs
    assert "![" in md and "](https://scienceops.lbto.org/wp-content/uploads/" in md


def test_extract_unwraps_layout_tables():
    url = "https://scienceops.lbto.org/lbti/instrument-characteristics/nomic-filters/"
    title, md = extract_main((FIXTURES / "nomic-filters.html").read_text(), url)
    assert title == "NOMIC filters"
    assert "sites-page-title-header" not in md
    assert "| Nprime | FW1 | 11.11 | 10.22 – 12.49 | Standard HOSTS filter |" in md
    assert md.splitlines()[0].startswith("## Overview")


def test_breadcrumbs_follow_navigation_tree():
    titles = {u: u.rstrip("/").split("/")[-1].title() for u in WEB_URLS}
    titles["https://scienceops.lbto.org/lbti/instrument-characteristics/"] = "Instrument Characteristics"
    titles[URL] = "LMIRCam Filters"
    crumbs = breadcrumbs(titles)
    assert crumbs[URL] == "Instrument Characteristics › LMIRCam Filters"


def test_sections_and_stable_ids():
    meta = {"url": URL, "title": "LMIRCam Filters", "breadcrumb": "Instrument Characteristics › LMIRCam Filters"}
    body = ("Intro text.\n\n## Overview {#TOC-Overview}\n\n### Broadband {#TOC-Broadband}\n\n| a | b |\n| --- | --- |\n"
            "| 1 | 2 |\n\n- item one\n- item two\n\n- item three\n\n#### Minor heading\n\nPara under minor.\n\n"
            "## Setup {#TOC-Setup}\n\nSetup text.")
    secs = split_sections(meta, body, "web", "lmircam-filters")
    ids = [s.id for s in secs]
    assert ids == ["web:lmircam-filters#lmircam-filters", "web:lmircam-filters#broadband", "web:lmircam-filters#setup"]
    assert ids == [s.id for s in split_sections(meta, body, "web", "lmircam-filters")]  # deterministic
    broad = secs[1]
    assert broad.source_url == URL + "#TOC-Broadband"
    assert broad.title == "Instrument Characteristics › LMIRCam Filters › Overview › Broadband"
    # citation units: table, merged list group, minor heading attached to its paragraph
    assert broad.paragraphs == ["| a | b |\n| --- | --- |\n| 1 | 2 |", "- item one\n- item two\n- item three",
                                "#### Minor heading\nPara under minor."]


def test_pdf_sections_use_page_ids():
    meta = {"url": "https://x.test/m.pdf", "title": "Manual PDF", "breadcrumb": "LBTI User's Manual PDF v0.11"}
    body = clean_pdf_pages(["## **LBTI user manual**\n\nfront", "_3_ _LBTI_\n\n#### **3.4 LMIRCam and ALES**\n\n"
                            "Text with 55 _._ 0 ms and Full ~~I~~ mage.\n\n##### **3.4.2 LMIRCam Detector**\n\nDetector.\n\n12"])
    assert "<!-- page: 2 -->" in body and "_3_ _LBTI_" not in body and "\n12" not in body
    assert "55.0 ms" in body and "Full Image" in body
    secs = split_sections(meta, body, "pdf", "LBTI_user_manual_v0.11")
    ids = [s.id for s in secs]
    assert "pdf:p2#3-4-lmircam-and-ales" in ids and "pdf:p2#3-4-2-lmircam-detector" in ids
    det = next(s for s in secs if s.id == "pdf:p2#3-4-2-lmircam-detector")
    assert det.source_url == "https://x.test/m.pdf#page=2"
    assert det.title.endswith("3.4 LMIRCam and ALES › 3.4.2 LMIRCam Detector")


def test_paragraphs_drop_page_markers():
    assert paragraphs_of("<!-- page: 3 -->\n\nHello\n\n<!-- page: 4 -->") == ["Hello"]
