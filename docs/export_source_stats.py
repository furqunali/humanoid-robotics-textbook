"""Deterministic per-source statistics for knowledge exports."""
from __future__ import annotations
from collections import Counter
from docs.knowledge_source import KnowledgeChunk

def summarize_sources(chunks: list[KnowledgeChunk]) -> dict[str, int]:
    return dict(sorted(Counter(chunk.source for chunk in chunks).items()))
