from dataclasses import dataclass
import re
from typing import Iterable


@dataclass(frozen=True)
class DocumentChunk:
    text: str
    source: str
    index: int


def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return re.sub(r"\s+", " ", text).strip()


def chunk_document(text: str, source: str, max_chars: int = 1200) -> list[DocumentChunk]:
    if not isinstance(source, str) or not source.strip():
        raise ValueError("source must be non-empty")
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    normalized = normalize_text(text)
    if not normalized:
        return []
    words = normalized.split(" ")
    chunks, current = [], []
    size = 0
    for word in words:
        extra = len(word) + (1 if current else 0)
        if current and size + extra > max_chars:
            chunks.append(DocumentChunk(" ".join(current), source.strip(), len(chunks)))
            current, size = [], 0
        if len(word) > max_chars:
            if current:
                chunks.append(DocumentChunk(" ".join(current), source.strip(), len(chunks)))
                current, size = [], 0
            chunks.append(DocumentChunk(word, source.strip(), len(chunks)))
            continue
        current.append(word)
        size += len(word) + (1 if size else 0)
    if current:
        chunks.append(DocumentChunk(" ".join(current), source.strip(), len(chunks)))
    return chunks


def chunk_many(documents: Iterable[tuple[str, str]], max_chars: int = 1200) -> list[DocumentChunk]:
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    result = []
    for text, source in documents:
        result.extend(chunk_document(text, source, max_chars))
    return result
