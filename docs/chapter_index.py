"""Deterministic chapter index for textbook navigation."""
from __future__ import annotations
from dataclasses import dataclass
@dataclass(frozen=True)
class ChapterEntry:
    title: str
    path: str
    order: int
def build_chapter_index(entries: list[ChapterEntry]) -> tuple[ChapterEntry, ...]:
    return tuple(sorted(entries, key=lambda item: (item.order, item.path, item.title)))
def chapter_paths(entries: list[ChapterEntry]) -> tuple[str, ...]:
    return tuple(entry.path for entry in build_chapter_index(entries))
