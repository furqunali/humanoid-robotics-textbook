"""Configuration helpers for the textbook vector store."""

from __future__ import annotations

import os
from dataclasses import dataclass


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
    return IngestConfig(qdrant_url=url, qdrant_api_key=api_key)
