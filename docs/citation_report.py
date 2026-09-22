"""Deterministic citation coverage report for textbook evidence."""
from __future__ import annotations

from dataclasses import dataclass

from docs.knowledge_source import KnowledgeChunk


@dataclass(frozen=True)
class CitationReport:
    total_chunks: int
    cited_chunks: int
    uncited_chunks: int
    coverage_rate: float

def build_citation_report(chunks: list[KnowledgeChunk], cited_ids: set[str]) -> CitationReport:
    known={chunk.id for chunk in chunks}
    cited=len(known & cited_ids)
    total=len(chunks)
    return CitationReport(total,cited,total-cited,round(cited/total,4) if total else 0.0)
