"""Build a deterministic, citation-ready knowledge source from textbook Markdown."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class KnowledgeChunk:
    id: str
    source: str
    title: str
    text: str
    index: int


def _clean(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def _title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def chunk_markdown(path: Path, max_chars: int = 1200) -> list[KnowledgeChunk]:
    if not isinstance(max_chars, int) or isinstance(max_chars, bool) or max_chars <= 0:
        raise ValueError("max_chars must be a positive integer")
    raw = path.read_text(encoding="utf-8")
    normalized = _clean(raw)
    if not normalized:
        return []
    words = normalized.split()
    chunks: list[KnowledgeChunk] = []
    current: list[str] = []
    size = 0
    title = _title(raw, path.stem)
    for word in words:
        extra = len(word) + (1 if current else 0)
        if current and size + extra > max_chars:
            text = " ".join(current)
            index = len(chunks)
            digest = hashlib.sha256(f"{path}:{index}:{text}".encode()).hexdigest()[:16]
            chunks.append(KnowledgeChunk(digest, path.as_posix(), title, text, index))
            current, size = [], 0
        current.append(word)
        size += len(word) + (1 if size else 0)
    if current:
        text = " ".join(current)
        index = len(chunks)
        digest = hashlib.sha256(f"{path}:{index}:{text}".encode()).hexdigest()[:16]
        chunks.append(KnowledgeChunk(digest, path.as_posix(), title, text, index))
    return chunks


def build_knowledge_source(root: Path, max_chars: int = 1200) -> list[KnowledgeChunk]:
    if not root.exists():
        raise FileNotFoundError(root)
    paths = sorted(root.rglob("*.md"))
    return [chunk for path in paths for chunk in chunk_markdown(path, max_chars)]


def write_jsonl(chunks: list[KnowledgeChunk], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8") as handle:
        for chunk in chunks:
            handle.write(json.dumps(asdict(chunk), ensure_ascii=False) + "\n")
