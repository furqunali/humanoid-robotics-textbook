from docs.citation_policy import CitationFinding
from docs.citation_summary import summarize_citations

def test_citation_summary_is_deterministic():
    findings = (CitationFinding("INCOMPLETE_COVERAGE", "error", "coverage"), CitationFinding("SOURCE_MISMATCH", "warning", "sources"))
    assert summarize_citations(findings) == (2, 1, 1, 0, False)
