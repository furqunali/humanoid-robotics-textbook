from docs.knowledge_length_median import median_chunk_length
from docs.knowledge_source import KnowledgeChunk


def test_median_chunk_length_for_odd_count():
    chunks = [KnowledgeChunk(str(i),"a.md","A","x"*n,i) for i,n in enumerate((2,5,9))]
    assert median_chunk_length(chunks) == 5.0

def test_median_chunk_length_for_even_count():
    chunks = [KnowledgeChunk(str(i),"a.md","A","x"*n,i) for i,n in enumerate((2,5,9,11))]
    assert median_chunk_length(chunks) == 7.0

def test_median_chunk_length_handles_empty_input():
    assert median_chunk_length([]) == 0.0
