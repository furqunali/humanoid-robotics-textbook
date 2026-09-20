"""Statistics for deterministic knowledge exports."""
from __future__ import annotations
from dataclasses import dataclass
from docs.knowledge_source import KnowledgeChunk

@dataclass(frozen=True)
class ExportStats:
    chunks: int
    sources: int
    characters: int
    average_characters: float

def summarize_export(chunks: list[KnowledgeChunk]) -> ExportStats:
    characters=sum(len(chunk.text) for chunk in chunks)
    sources=len({chunk.source for chunk in chunks})
    return ExportStats(len(chunks),sources,characters,round(characters/len(chunks),2) if chunks else 0.0)
