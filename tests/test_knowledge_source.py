from pathlib import Path

from docs.knowledge_source import build_knowledge_source, chunk_markdown, write_jsonl


def test_chunk_markdown_has_stable_citation_fields(tmp_path: Path):
    path = tmp_path / "robotics.md"
    path.write_text("# Humanoid Robotics\n\nA robot walks using control.", encoding="utf-8")
    chunks = chunk_markdown(path, max_chars=100)
    assert len(chunks) == 1
    assert chunks[0].source == path.as_posix()
    assert chunks[0].title == "Humanoid Robotics"
    assert chunks[0].id == chunk_markdown(path, max_chars=100)[0].id


def test_build_knowledge_source_is_sorted_and_recursive(tmp_path: Path):
    (tmp_path / "b.md").write_text("# B\ntext", encoding="utf-8")
    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "a.md").write_text("# A\ntext", encoding="utf-8")
    chunks = build_knowledge_source(tmp_path)
    assert [c.source for c in chunks] == sorted(c.source for c in chunks)


def test_write_jsonl_round_trips_records(tmp_path: Path):
    source = tmp_path / "a.md"
    source.write_text("# A\ntext", encoding="utf-8")
    chunks = chunk_markdown(source)
    output = tmp_path / "knowledge" / "corpus.jsonl"
    write_jsonl(chunks, output)
    lines = output.read_text(encoding="utf-8").splitlines()
    assert len(lines) == len(chunks)
    assert '"source"' in lines[0]
    assert '"id"' in lines[0]


def test_chunk_markdown_rejects_non_integer_max_chars(tmp_path: Path):
    path = tmp_path / "robotics.md"
    path.write_text("# Robotics\ntext", encoding="utf-8")
    import pytest
    with pytest.raises(ValueError, match="positive integer"):
        chunk_markdown(path, max_chars=10.5)
    with pytest.raises(ValueError, match="positive integer"):
        chunk_markdown(path, max_chars=True)
