from docs.citation_policy import CitationFinding
from docs.citation_policy_json import to_json

def test_citation_policy_json_is_stable():
    findings = (CitationFinding("INCOMPLETE_COVERAGE", "error", "citation coverage is 0.5000"),)
    assert to_json(findings) == '[{"code":"INCOMPLETE_COVERAGE","message":"citation coverage is 0.5000","severity":"error"}]'
