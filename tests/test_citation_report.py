from docs.citation_report import build_citation_report
from docs.knowledge_source import KnowledgeChunk


def test_citation_report_calculates_coverage():
    chunks=[KnowledgeChunk("a","x.md","X","one",0),KnowledgeChunk("b","x.md","X","two",1)]
    report=build_citation_report(chunks,{"a"})
    assert report.cited_chunks==1
    assert report.uncited_chunks==1
    assert report.coverage_rate==0.5

def test_unknown_citations_do_not_inflate_coverage():
    chunks=[KnowledgeChunk("a","x.md","X","one",0)]
    assert build_citation_report(chunks,{"unknown"}).coverage_rate==0.0
