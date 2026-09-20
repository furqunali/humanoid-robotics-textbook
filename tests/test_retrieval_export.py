from pathlib import Path
import pytest
from docs.knowledge_source import KnowledgeChunk
from docs.retrieval_export import export_retrieval_chunks

def c(i): return KnowledgeChunk(str(i), "chapter.md", "Chapter", "text", i)

def test_export_is_sorted_and_counted(tmp_path: Path):
    out=tmp_path/"chunks.jsonl"
    assert export_retrieval_chunks([c(1),c(0)],out)==2
    lines=out.read_text(encoding="utf-8").splitlines()
    assert '"index": 0' in lines[0]

def test_export_rejects_duplicates(tmp_path: Path):
    with pytest.raises(ValueError, match="duplicate"):
        export_retrieval_chunks([c(0),c(0)],tmp_path/"x")
