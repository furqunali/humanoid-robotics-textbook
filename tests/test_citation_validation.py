from docs.citation_index import CitationRecord
from docs.citation_validation import require_valid_citations, validate_citations


def record(chunk_id: str) -> CitationRecord:
    return CitationRecord(chunk_id, "chapter.md", "Chapter", 0, "chapter#0")


def test_validation_returns_unknown_ids_sorted():
    assert validate_citations(["b", "missing", "a"], [record("a"), record("b")]) == ["missing"]


def test_validation_accepts_known_ids():
    require_valid_citations(["a", "b"], [record("a"), record("b")])


def test_validation_rejects_unknown_ids():
    try:
        require_valid_citations(["missing"], [record("a")])
    except ValueError as exc:
        assert "missing" in str(exc)
    else:
        raise AssertionError("expected unknown citation to fail")
