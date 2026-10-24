from __future__ import annotations

from scripts.ingest import WEB_URLS, breadcrumbs, extract_main
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
