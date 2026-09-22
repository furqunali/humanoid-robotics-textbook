"""Deterministic statistics for the generated knowledge corpus."""
from __future__ import annotations

from dataclasses import dataclass

from docs.knowledge_source import KnowledgeChunk


@dataclass(frozen=True)
class KnowledgeStats:
    chunks: int
    sources: int
    total_characters: int
    average_characters: float
    empty_chunks: int


def summarize_chunks(chunks: list[KnowledgeChunk]) -> KnowledgeStats:
    """Return stable corpus-size metrics without changing source ordering."""
    if any(not isinstance(chunk, KnowledgeChunk) for chunk in chunks):
        raise TypeError("chunks must contain KnowledgeChunk values")
    total = sum(len(chunk.text) for chunk in chunks)
    return KnowledgeStats(
        chunks=len(chunks),
        sources=len({chunk.source for chunk in chunks}),
        total_characters=total,
        average_characters=round(total / len(chunks), 2) if chunks else 0.0,
        empty_chunks=sum(not chunk.text.strip() for chunk in chunks),
    )
