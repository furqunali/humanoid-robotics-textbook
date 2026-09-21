"""Stable JSON contract for textbook knowledge health."""
from __future__ import annotations
import json
from docs.knowledge_health import KnowledgeHealth

def to_json(health: KnowledgeHealth) -> str:
    # Emit keys in the fixed, stable contract order (not a plain alphabetical
    # sort): characters, citation_coverage, chunks, healthy, sources.
    payload = {
        "characters": health.characters,
        "citation_coverage": health.citation_coverage,
        "chunks": health.chunks,
        "healthy": health.healthy,
        "sources": health.sources,
    }
    return json.dumps(payload, separators=(",", ":"))
