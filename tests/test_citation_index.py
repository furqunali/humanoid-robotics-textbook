from pathlib import Path

import pytest

from docs.citation_index import build_citation_index, write_citation_index
from docs.knowledge_source import KnowledgeChunk


def chunk(cid: str, source: str = "chapters/intro.md", index: int = 0) -> KnowledgeChunk:
    return KnowledgeChunk(cid, source, "Intro", "grounded text", index)


def test_build_index_is_sorted_and_stable():
    records = build_citation_index([chunk("b", index=1), chunk("a")])
    assert [record.chunk_id for record in records] == ["a", "b"]
    assert records[0].anchor == "intro#0"


def test_duplicate_ids_are_rejected():
    with pytest.raises(ValueError, match="duplicate"):
        build_citation_index([chunk("same"), chunk("same")])


def test_invalid_chunk_fields_are_rejected():
    with pytest.raises(ValueError):
        build_citation_index([chunk("")])
    with pytest.raises(ValueError):
        build_citation_index([chunk("ok", index=-1)])


def test_write_index_is_deterministic(tmp_path: Path):
    records = build_citation_index([chunk("b", index=1), chunk("a")])
    destination = tmp_path / "index.jsonl"
    write_citation_index(records, destination)
    lines = destination.read_text(encoding="utf-8").splitlines()
    assert '"chunk_id": "a"' in lines[0]
    assert '"chunk_id": "b"' in lines[1]
