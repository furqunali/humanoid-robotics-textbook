from docs.knowledge_source import KnowledgeChunk
from docs.knowledge_stats import summarize_chunks


def chunk(source: str, index: int, text: str) -> KnowledgeChunk:
    return KnowledgeChunk(f"{source}-{index}", source, f"Title {index}", text, index)


def test_summarize_chunks_counts_sources_and_characters():
    result = summarize_chunks([chunk("a.md", 0, "abc"), chunk("a.md", 1, "de"), chunk("b.md", 0, "f")])
    assert result.chunks == 3
    assert result.sources == 2
    assert result.total_characters == 6
    assert result.average_characters == 2.0
    assert result.empty_chunks == 0


def test_summarize_chunks_handles_empty_corpus():
    result = summarize_chunks([])
    assert result.chunks == 0
    assert result.sources == 0
    assert result.average_characters == 0.0


def test_summarize_chunks_tracks_empty_text():
    result = summarize_chunks([chunk("a.md", 0, " "), chunk("a.md", 1, "ok")])
    assert result.empty_chunks == 1
