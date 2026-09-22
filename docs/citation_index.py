"""Build a deterministic citation index over knowledge chunks.

The index is intentionally small and JSON-serializable so downstream RAG
services can resolve a chunk id back to its source and human-readable title.
"""
from __future__ import annotations

import json
import re
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from pathlib import Path

from docs.knowledge_source import KnowledgeChunk


@dataclass(frozen=True)
class CitationRecord:
    chunk_id: str
    source: str
    title: str
    index: int
    anchor: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def _anchor(source: str, index: int) -> str:
    stem = Path(source).stem
    slug = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return f"{slug}#{index}"


def build_citation_index(chunks: Iterable[KnowledgeChunk]) -> list[CitationRecord]:
    """Create a stable, duplicate-free citation index from chunks."""
    records: list[CitationRecord] = []
    seen: set[str] = set()
    for chunk in chunks:
        if not chunk.id or not chunk.source:
            raise ValueError("chunks require non-empty id and source")
        if chunk.id in seen:
            raise ValueError(f"duplicate chunk id: {chunk.id}")
        if chunk.index < 0:
            raise ValueError("chunk index must be non-negative")
        seen.add(chunk.id)
        records.append(
            CitationRecord(
                chunk_id=chunk.id,
                source=chunk.source,
                title=chunk.title,
                index=chunk.index,
                anchor=_anchor(chunk.source, chunk.index),
            )
        )
    return sorted(records, key=lambda record: (record.source, record.index, record.chunk_id))


def write_citation_index(records: Iterable[CitationRecord], destination: Path) -> None:
    """Write one JSON object per line in deterministic order."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(records, key=lambda record: (record.source, record.index, record.chunk_id))
    with destination.open("w", encoding="utf-8") as handle:
        for record in ordered:
            handle.write(json.dumps(record.to_dict(), ensure_ascii=False, sort_keys=True))
            handle.write("\n")
