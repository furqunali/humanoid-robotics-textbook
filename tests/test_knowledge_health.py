from docs.citation_report import CitationReport
from docs.export_stats import ExportStats
from docs.knowledge_health import build_health


def test_health_requires_complete_citation_coverage():
    stats = ExportStats(4, 2, 100, 25.0)
    report = CitationReport(4, 4, 0, 1.0)
    health = build_health(stats, report)
    assert health.healthy
    assert health.citation_coverage == 1.0
