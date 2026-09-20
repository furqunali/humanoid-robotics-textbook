from docs.citation_policy import evaluate_citations
from docs.knowledge_health import KnowledgeHealth

def test_citation_policy_reports_incomplete_coverage():
    health = KnowledgeHealth(4, 2, 100, 0.75, False)
    findings = evaluate_citations(health)
    assert findings[0].code == "INCOMPLETE_COVERAGE"
    assert findings[0].severity == "error"

def test_citation_policy_reports_healthy_export():
    health = KnowledgeHealth(4, 2, 100, 1.0, True)
    assert evaluate_citations(health)[0].code == "HEALTHY"


def test_multiple_chunks_per_source_do_not_trigger_source_mismatch():
    health = KnowledgeHealth(12, 2, 1000, 1.0, True)
    assert evaluate_citations(health)[0].code == "HEALTHY"
