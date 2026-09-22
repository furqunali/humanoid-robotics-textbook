"""Deterministic citation coverage metrics for grounded answers."""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from docs.citation_index import CitationRecord


@dataclass(frozen=True)
class CitationCoverage:
    cited: int
    known: int
    coverage: float


def measure_citation_coverage(
    citations: Iterable[str], records: Iterable[CitationRecord]
) -> CitationCoverage:
    """Measure unique known citations against the available source index."""
    known_ids = {record.chunk_id for record in records}
    cited_ids = {citation for citation in citations if citation in known_ids}
    coverage = round(len(cited_ids) / len(known_ids), 4) if known_ids else 0.0
    return CitationCoverage(len(cited_ids), len(known_ids), coverage)
