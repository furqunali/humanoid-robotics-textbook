"""Small reusable validators for ingestion metadata."""
from __future__ import annotations
from urllib.parse import urlparse

def validate_source_label(label: str) -> str:
    """Normalize a human-readable source label."""
    value = (label or "").strip()
    if not value:
        raise ValueError("source label must not be empty")
    if len(value) > 200:
        raise ValueError("source label must be at most 200 characters")
    return value

def validate_source_scheme(url: str) -> str:
    """Return the normalized scheme for an HTTP(S) source URL."""
    value = (url or "").strip()
    scheme = urlparse(value).scheme.lower()
    if scheme not in {"http", "https"}:
        raise ValueError("source URL must use HTTP or HTTPS")
    return scheme
