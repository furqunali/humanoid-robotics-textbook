from docs.knowledge_cli import export_knowledge


def test_export_knowledge_writes_deterministic_jsonl(tmp_path):
    root = tmp_path / "book"
    root.mkdir()
    (root / "Chapter1.md").write_text("# Intro\n\nGrounded robotics.", encoding="utf-8")
    output = tmp_path / "out.jsonl"
    count = export_knowledge(root, output)
    assert count == 1
    assert output.read_text(encoding="utf-8").count("\n") == 1

def test_export_rejects_invalid_limit(tmp_path):
    root = tmp_path / "book"
    root.mkdir()
    try:
        export_knowledge(root, tmp_path / "out.jsonl", 0)
    except ValueError as exc:
        assert "max_chars" in str(exc)
    else:
        raise AssertionError("expected ValueError")
