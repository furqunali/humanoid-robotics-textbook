"""Deterministic length statistics for textbook knowledge chunks."""
from __future__ import annotations
from dataclasses import dataclass
from .knowledge_source import KnowledgeChunk

@dataclass(frozen=True)
class LengthProfile:
    chunks: int
    minimum: int
    maximum: int
    average: float

def profile_chunk_lengths(chunks: list[KnowledgeChunk]) -> LengthProfile:
    lengths = [len(chunk.text) for chunk in chunks]
    if not lengths:
        return LengthProfile(0, 0, 0, 0.0)
    return LengthProfile(len(lengths), min(lengths), max(lengths), round(sum(lengths) / len(lengths), 2))
