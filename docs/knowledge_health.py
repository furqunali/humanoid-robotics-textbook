"""Deterministic health summary for textbook knowledge exports."""
from __future__ import annotations

from dataclasses import dataclass

from docs.citation_report import CitationReport
from docs.export_stats import ExportStats


@dataclass(frozen=True)
class KnowledgeHealth:
    chunks: int
    sources: int
    characters: int
    citation_coverage: float
    healthy: bool

def build_health(stats: ExportStats, citations: CitationReport) -> KnowledgeHealth:
    healthy = (
        stats.chunks == citations.total_chunks
        and citations.uncited_chunks == 0
    )
    return KnowledgeHealth(
        chunks=stats.chunks,
        sources=stats.sources,
        characters=stats.characters,
        citation_coverage=citations.coverage_rate,
        healthy=healthy,
    )
