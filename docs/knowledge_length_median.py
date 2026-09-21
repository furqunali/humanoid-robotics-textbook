"""Deterministic median length metric for textbook chunks."""
from __future__ import annotations
from statistics import median
from .knowledge_source import KnowledgeChunk

def median_chunk_length(chunks: list[KnowledgeChunk]) -> float:
    lengths = [len(chunk.text) for chunk in chunks]
    return float(median(lengths)) if lengths else 0.0
