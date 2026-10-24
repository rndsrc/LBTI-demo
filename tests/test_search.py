from __future__ import annotations

from app.search import Manual, fts_query


def test_fts_query_quotes_terms():
    assert fts_query('What are the "NOMIC" filters?') == '"nomic" OR "filters"'
    assert fts_query("") is None
    assert fts_query('NOT ( ) * nomic"') == '"not" OR "nomic"'  # FTS operators become plain terms


def test_nomic_ranks_the_nomic_filters_section_first(cfg):
    manual = Manual(cfg.index_dir)
    assert [s["id"] for s in manual.search("NOMIC")][0] == "web:nomic-filters#overview"
    assert manual.search("zzzqqq") == []
