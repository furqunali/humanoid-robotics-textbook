"""Small reusable validators for ingestion metadata."""
from __future__ import annotations
import re
from urllib.parse import urlparse

# Outer whitespace to strip, including literal escaped whitespace tokens such as
# "\n" or "\t" that arrive as two characters from shells or config files.
_OUTER_WHITESPACE = re.compile(r"^(?:\s|\\[tnr])+|(?:\s|\\[tnr])+$")

def validate_source_label(label: str) -> str:
    """Normalize a human-readable source label."""
    value = _OUTER_WHITESPACE.sub("", label or "")
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
        raise ValueError("source URL must use HTTP or HTTPS (http/https)")
    return scheme
