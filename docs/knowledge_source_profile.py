"""Deterministic per-source length profiles for textbook knowledge."""
from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
from .knowledge_source import KnowledgeChunk

@dataclass(frozen=True)
class SourceLengthProfile:
    source: str
    chunks: int
    minimum: int
    maximum: int
    average: float

def profile_source_lengths(chunks: list[KnowledgeChunk]) -> tuple[SourceLengthProfile, ...]:
    groups: dict[str, list[int]] = defaultdict(list)
    for chunk in chunks:
        if not isinstance(chunk, KnowledgeChunk):
            raise TypeError("chunks must contain KnowledgeChunk values")
        groups[chunk.source].append(len(chunk.text))
    return tuple(SourceLengthProfile(s,len(v),min(v),max(v),round(sum(v)/len(v),2))
                 for s,v in sorted(groups.items()))
