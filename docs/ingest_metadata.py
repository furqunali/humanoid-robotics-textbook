"""Stable metadata validation for textbook ingestion."""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class DocumentMetadata:
    source: str
    title: str
    section: str

def validate_metadata(source: str, title: str, section: str) -> DocumentMetadata:
    values = {"source": source, "title": title, "section": section}
    if any(not isinstance(v, str) or not v.strip() for v in values.values()):
        raise ValueError("source, title, and section must be non-empty strings")
    return DocumentMetadata(source=source.strip(), title=title.strip(), section=section.strip())
