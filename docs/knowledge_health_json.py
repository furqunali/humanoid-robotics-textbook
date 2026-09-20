"""Stable JSON contract for textbook knowledge health."""
from __future__ import annotations
from dataclasses import asdict
import json
from docs.knowledge_health import KnowledgeHealth

def to_json(health: KnowledgeHealth) -> str:
    return json.dumps(asdict(health), sort_keys=True, separators=(",", ":"))
