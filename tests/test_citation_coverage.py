from docs.citation_coverage import measure_citation_coverage
from docs.citation_index import CitationRecord


def record(chunk_id: str) -> CitationRecord:
    return CitationRecord(chunk_id, "chapter.md", "Chapter", 0, "chapter")


def test_measure_citation_coverage_uses_unique_known_ids():
    result = measure_citation_coverage(["a", "a", "missing"], [record("a"), record("b")])
    assert result.cited == 1
    assert result.known == 2
    assert result.coverage == 0.5


def test_measure_citation_coverage_handles_empty_index():
    result = measure_citation_coverage(["a"], [])
    assert result.cited == 0
    assert result.known == 0
    assert result.coverage == 0.0
