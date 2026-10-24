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


def test_search_tool_returns_citable_sections(cfg):
    manual = Manual(cfg.index_dir)
    result = manual.run_tool({"query": "Br-alpha"})[0]
    assert result["type"] == "search_result" and result["citations"] == {"enabled": True}
    assert result["source"] == "https://example.test/lbti/instrument-characteristics/lmircam-filters/#TOC-Narrowband-filters"
    assert result["title"] == "Instrument Characteristics › LMIRCam Filters › Narrowband filters"
    assert [b["text"] for b in result["content"]][1] == "LMIRCam can be used together with NOMIC through the dichroic."
    assert manual.run_tool({"query": "zzzqqq"}) == [{"type": "text", "text": "No matching sections found."}]
    assert manual.run_tool({}) == [{"type": "text", "text": "No matching sections found."}]
