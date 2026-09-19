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
    if not url or not api_key:
        raise RuntimeError("QDRANT_URL and QDRANT_API_KEY are required")
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("QDRANT_URL must be a valid HTTP(S) URL")
    return IngestConfig(qdrant_url=url, qdrant_api_key=api_key)


def validate_source_url(url: str) -> str:
    """Validate and normalize an ingestion source URL."""
    value = (url or "").strip()
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("source URL must be a valid HTTP(S) URL")
    return value
