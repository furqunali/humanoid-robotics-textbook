from docs.knowledge_source import KnowledgeChunk
from docs.chunk_quality_gate import evaluate_chunk_quality

def c(i,text): return KnowledgeChunk(str(i),"a.md","A",text,i)

def test_chunk_bounds():
    gate = evaluate_chunk_quality([c(0,"abc"),c(1,"abcd")], minimum=3, maximum=4)
    assert gate.passed and gate.chunks == 2

def test_oversized_fails():
    gate = evaluate_chunk_quality([c(0,"abcdef")], maximum=5)
    assert gate.passed is False and gate.oversized == 1
