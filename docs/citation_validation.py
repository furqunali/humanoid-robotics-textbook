"""Validate generated citation references against the deterministic index."""
from __future__ import annotations

from collections.abc import Iterable

from docs.citation_index import CitationRecord


def validate_citations(
    citations: Iterable[str],
    records: Iterable[CitationRecord],
) -> list[str]:
    """Return unknown citation ids in deterministic order."""
    known = {record.chunk_id for record in records}
    unknown = sorted({citation for citation in citations if citation not in known})
    return unknown


def require_valid_citations(
    citations: Iterable[str],
    records: Iterable[CitationRecord],
) -> None:
    """Raise when a response cites a chunk absent from the source index."""
    unknown = validate_citations(citations, records)
    if unknown:
        raise ValueError(f"unknown citation ids: {', '.join(unknown)}")
