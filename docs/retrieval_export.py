"""Export knowledge chunks in a compact retrieval-oriented JSONL format."""
from __future__ import annotations

import json
from pathlib import Path

from docs.knowledge_source import KnowledgeChunk


def export_retrieval_chunks(chunks: list[KnowledgeChunk], destination: Path) -> int:
    seen: set[str] = set()
    destination.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with destination.open("w", encoding="utf-8") as handle:
        for chunk in sorted(chunks, key=lambda item: (item.source, item.index, item.id)):
            if chunk.id in seen:
                raise ValueError(f"duplicate chunk id: {chunk.id}")
            if not chunk.text.strip():
                raise ValueError(f"empty chunk: {chunk.id}")
            seen.add(chunk.id)
            payload = {"id": chunk.id, "text": chunk.text, "source": chunk.source,
                       "title": chunk.title, "index": chunk.index}
            handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
            count += 1
    return count
