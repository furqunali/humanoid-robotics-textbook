from docs.knowledge_length_profile import profile_chunk_lengths
from docs.knowledge_source import KnowledgeChunk
import pytest

def test_length_profile_reports_range_and_average():
    chunks = [KnowledgeChunk("a","a.md","A","abc",0), KnowledgeChunk("b","a.md","A","abcdef",1)]
    p = profile_chunk_lengths(chunks)
    assert (p.chunks, p.minimum, p.maximum, p.average, p.over_limit) == (2, 3, 6, 4.5, 0)

def test_length_profile_counts_chunks_over_limit():
    chunks = [KnowledgeChunk("a","a.md","A","abc",0), KnowledgeChunk("b","a.md","A","abcdef",1)]
    assert profile_chunk_lengths(chunks, max_chars=5).over_limit == 1

def test_length_profile_rejects_invalid_limit():
    with pytest.raises(ValueError, match="max_chars"):
        profile_chunk_lengths([], max_chars=0)

def test_length_profile_handles_empty_corpus():
    assert profile_chunk_lengths([]).maximum == 0
