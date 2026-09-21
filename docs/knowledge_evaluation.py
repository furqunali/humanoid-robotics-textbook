"""Quality checks for deterministic textbook knowledge sources."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from .knowledge_source import KnowledgeChunk

@dataclass(frozen=True)
class KnowledgeReport:
    chunks: int
    sources: int
    duplicate_ids: tuple[str, ...]
    empty_chunks: int
    max_length: int
    oversized_chunks: int

    @property
    def valid(self) -> bool:
        return not self.duplicate_ids and self.empty_chunks == 0 and self.oversized_chunks == 0

def evaluate_chunks(chunks: list[KnowledgeChunk], max_chars: int = 1200) -> KnowledgeReport:
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    duplicate_ids = tuple(sorted(k for k, n in Counter(c.id for c in chunks).items() if n > 1))
    empty = sum(1 for c in chunks if not c.text.strip())
    oversized = sum(1 for c in chunks if len(c.text) > max_chars)
    return KnowledgeReport(
        chunks=len(chunks),
        sources=len({c.source for c in chunks}),
        duplicate_ids=duplicate_ids,
        empty_chunks=empty,
        max_length=max((len(c.text) for c in chunks), default=0),
        oversized_chunks=oversized,
    )
