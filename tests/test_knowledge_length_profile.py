from docs.knowledge_length_profile import profile_chunk_lengths
from docs.knowledge_source import KnowledgeChunk

def test_length_profile_reports_range_and_average():
    chunks = [KnowledgeChunk("a","a.md","A","abc",0), KnowledgeChunk("b","a.md","A","abcdef",1)]
    p = profile_chunk_lengths(chunks)
    assert (p.chunks, p.minimum, p.maximum, p.average) == (2, 3, 6, 4.5)

def test_length_profile_handles_empty_corpus():
    assert profile_chunk_lengths([]).maximum == 0
