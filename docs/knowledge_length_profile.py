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
    over_limit: int

def profile_chunk_lengths(chunks: list[KnowledgeChunk], *, max_chars: int | None = None) -> LengthProfile:
    if max_chars is not None and max_chars <= 0:
        raise ValueError("max_chars must be positive")
    lengths = [len(chunk.text) for chunk in chunks]
    if not lengths:
        return LengthProfile(0, 0, 0, 0.0, 0)
    over_limit = sum(length > max_chars for length in lengths) if max_chars is not None else 0
    return LengthProfile(len(lengths), min(lengths), max(lengths), round(sum(lengths) / len(lengths), 2), over_limit)
