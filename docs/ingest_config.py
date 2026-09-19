"""Configuration helpers for the textbook vector store."""

from __future__ import annotations

import os
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen=True)
class IngestConfig:
    qdrant_url: str
    qdrant_api_key: str
    collection_name: str = "robotics_textbook"
    vector_size: int = 1536


def load_config() -> IngestConfig:
    url = os.getenv("QDRANT_URL", "").strip()
    api_key = os.getenv("QDRANT_API_KEY", "").strip()
    collection_name = os.getenv("QDRANT_COLLECTION", "robotics_textbook").strip()
    vector_size_raw = os.getenv("QDRANT_VECTOR_SIZE", "1536").strip()

    if not url or not api_key:
        raise RuntimeError("QDRANT_URL and QDRANT_API_KEY are required")

    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("QDRANT_URL must be a valid HTTP(S) URL")

    if not collection_name:
        raise ValueError("QDRANT_COLLECTION must not be empty")

    try:
        vector_size = int(vector_size_raw)
    except ValueError as exc:
        raise ValueError("QDRANT_VECTOR_SIZE must be an integer") from exc

    if vector_size <= 0:
        raise ValueError("QDRANT_VECTOR_SIZE must be positive")

    return IngestConfig(
        qdrant_url=url,
        qdrant_api_key=api_key,
        collection_name=collection_name,
        vector_size=vector_size,
    )


def validate_source_url(url: str) -> str:
    """Validate and normalize an ingestion source URL."""
    value = (url or "").strip()
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("source URL must be a valid HTTP(S) URL")
    return value
