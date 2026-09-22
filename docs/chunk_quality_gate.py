"""Deterministic chunk-size gate for textbook knowledge."""
from __future__ import annotations

from dataclasses import dataclass

from .knowledge_source import KnowledgeChunk


@dataclass(frozen=True)
class ChunkQualityGate:
    chunks: int
    oversized: int
    undersized: int
    passed: bool

def evaluate_chunk_quality(chunks: list[KnowledgeChunk], *, minimum: int = 1, maximum: int = 1200) -> ChunkQualityGate:
    if minimum < 0 or maximum < minimum:
        raise ValueError("invalid chunk bounds")
    lengths = []
    for chunk in chunks:
        if not isinstance(chunk, KnowledgeChunk):
            raise TypeError("chunks must contain KnowledgeChunk values")
        lengths.append(len(chunk.text))
    oversized = sum(length > maximum for length in lengths)
    undersized = sum(length < minimum for length in lengths)
    return ChunkQualityGate(len(lengths), oversized, undersized, oversized == 0 and undersized == 0)
