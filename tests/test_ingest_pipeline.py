import pytest

from docs.ingest_pipeline import chunk_document, normalize_text


def test_normalize_text_collapses_whitespace():
    assert normalize_text("  humanoid\n  robotics   lab ") == "humanoid robotics lab"


def test_chunk_document_preserves_source_and_order():
    chunks = chunk_document("one two three four", "docs/intro.md", max_chars=7)
    assert [chunk.index for chunk in chunks] == [0, 1, 2]
    assert all(chunk.source == "docs/intro.md" for chunk in chunks)


def test_chunk_document_rejects_invalid_size():
    with pytest.raises(ValueError):
        chunk_document("robotics", "docs/intro.md", max_chars=0)
