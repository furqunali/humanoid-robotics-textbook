from docs.citation_policy import CitationFinding
from docs.citation_summary import summarize_citations

def test_citation_summary_is_deterministic():
    findings = (CitationFinding("INCOMPLETE_COVERAGE", "error", "coverage"), CitationFinding("SOURCE_MISMATCH", "warning", "sources"))
    summary = summarize_citations(findings)
    assert summary.total == 2
    assert summary.errors == 1
    assert summary.warnings == 1
    assert summary.infos == 0
    assert not summary.covered
