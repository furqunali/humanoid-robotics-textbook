"""Validation for vector-ingestion configuration values."""
from __future__ import annotations


def validate_ingest_config(config) -> bool:
    if not getattr(config, "collection_name", "").strip():
        raise ValueError("collection_name must be non-empty")
    if not isinstance(getattr(config, "vector_size", None), int) or config.vector_size <= 0:
        raise ValueError("vector_size must be a positive integer")
    return True
