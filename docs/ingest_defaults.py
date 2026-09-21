"""Defaults and normalization helpers for textbook ingestion settings."""
from __future__ import annotations

import re

DEFAULT_COLLECTION = "robotics_textbook"
DEFAULT_VECTOR_SIZE = 1536

# Outer whitespace to strip, including literal escaped whitespace tokens such as
# "\t" or "\n" that arrive from shells or config files as two characters.
_OUTER_WHITESPACE = re.compile(r"^(?:\s|\\[tnr])+|(?:\s|\\[tnr])+$")

def normalize_collection_name(value: str | None) -> str:
    """Return a configured collection name or the documented default."""
    normalized = _OUTER_WHITESPACE.sub("", value or "")
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
