"""Defaults and normalization helpers for textbook ingestion settings."""
from __future__ import annotations

DEFAULT_COLLECTION = "robotics_textbook"
DEFAULT_VECTOR_SIZE = 1536

def normalize_collection_name(value: str | None) -> str:
    """Return a configured collection name or the documented default."""
    normalized = (value or "").strip()
    return normalized or DEFAULT_COLLECTION

def parse_vector_size(value: str | None) -> int:
    """Parse vector size while keeping validation close to configuration."""
    normalized = (value or "").strip()
    if not normalized:
        return DEFAULT_VECTOR_SIZE
    try:
        size = int(normalized)
    except ValueError as exc:
        raise ValueError("vector size must be an integer") from exc
    if size <= 0:
        raise ValueError("vector size must be positive")
    return size
