import pytest

from docs.ingest_pipeline import chunk_document, chunk_many, normalize_text


def test_normalize_text_collapses_whitespace():
    assert normalize_text("  humanoid\n  robotics   lab ") == "humanoid robotics lab"


def test_chunk_document_preserves_source_and_order():
    chunks = chunk_document("one two three four", "docs/intro.md", max_chars=7)
    assert [chunk.index for chunk in chunks] == [0, 1, 2]
    assert all(chunk.source == "docs/intro.md" for chunk in chunks)


def test_chunk_document_rejects_invalid_size():
    with pytest.raises(ValueError):
        chunk_document("robotics", "docs/intro.md", max_chars=0)


def test_chunk_document_handles_words_longer_than_limit():
    chunks = chunk_document("short supercalifragilistic", "docs/intro.md", max_chars=5)
    assert [chunk.text for chunk in chunks] == ["short", "supercalifragilistic"]


def test_chunk_many_rejects_invalid_size_even_when_empty():
    with pytest.raises(ValueError):
        chunk_many([], max_chars=0)


def test_chunk_document_rejects_noninteger_size():
    for value in (1.5, True):
        with pytest.raises(ValueError):
            chunk_document("robotics", "docs/intro.md", max_chars=value)
