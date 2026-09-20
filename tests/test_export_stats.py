from docs.export_stats import summarize_export
from docs.knowledge_source import KnowledgeChunk

def test_export_stats_summarizes_corpus():
    chunks=[KnowledgeChunk("a","x.md","X","one",0),KnowledgeChunk("b","y.md","Y","1234",0)]
    stats=summarize_export(chunks)
    assert stats.chunks==2
    assert stats.sources==2
    assert stats.characters==7
    assert stats.average_characters==3.5

def test_export_stats_empty():
    assert summarize_export([]).average_characters==0.0
