from docs.export_source_stats import summarize_sources
from docs.knowledge_source import KnowledgeChunk


def test_source_stats_are_sorted_and_counted():
    chunks=[KnowledgeChunk("1","z.md","Z","x",0),KnowledgeChunk("2","a.md","A","y",0),KnowledgeChunk("3","z.md","Z","z",1)]
    assert summarize_sources(chunks)=={"a.md":1,"z.md":2}

def test_source_stats_empty():
    assert summarize_sources([])=={}
