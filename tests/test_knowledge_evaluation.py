from docs.knowledge_evaluation import evaluate_chunks
from docs.knowledge_source import KnowledgeChunk
import pytest

def test_evaluate_chunks_reports_valid_corpus():
    chunks = [KnowledgeChunk("a", "docs/a.md", "A", "robot", 0),
              KnowledgeChunk("b", "docs/b.md", "B", "control", 0)]
    report = evaluate_chunks(chunks)
    assert report.valid
    assert report.chunks == 2
    assert report.sources == 2
    assert report.oversized_chunks == 0

def test_evaluate_chunks_detects_duplicate_ids_and_empty_text():
    chunks = [KnowledgeChunk("same", "a.md", "A", "", 0),
              KnowledgeChunk("same", "b.md", "B", "x", 0)]
    report = evaluate_chunks(chunks)
    assert report.valid is False
    assert report.duplicate_ids == ("same",)
    assert report.empty_chunks == 1

def test_evaluate_chunks_detects_oversized_chunks():
    chunks = [KnowledgeChunk("a", "a.md", "A", "12345", 0)]
    report = evaluate_chunks(chunks, max_chars=4)
    assert report.oversized_chunks == 1
    assert report.valid is False

def test_evaluate_chunks_rejects_non_positive_limit():
    with pytest.raises(ValueError, match="positive"):
        evaluate_chunks([], max_chars=0)
