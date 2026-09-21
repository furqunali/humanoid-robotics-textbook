"""Create a machine-readable manifest for textbook Markdown chapters."""
from __future__ import annotations
from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Iterable

@dataclass(frozen=True)
class ChapterEntry:
    path: str
    title: str
    bytes: int
    words: int
    sections: int
    def to_dict(self) -> dict[str, object]:
        return asdict(self)

def chapter_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip() or fallback
    return fallback

def section_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.startswith("## "))

def word_count(text: str) -> int:
    """Count content words, excluding the H1 title's ``#`` sigil.

    The document title is captured separately from the leading ``# `` heading,
    so its marker is not counted as a word; other content is counted verbatim.
    """
    tokens: list[str] = []
    for line in text.splitlines():
        if line.startswith("# "):
            line = line[2:]
        tokens.extend(line.split())
    return len(tokens)

def build_manifest(root: Path, paths: Iterable[Path] | None = None) -> list[ChapterEntry]:
    if not root.exists():
        raise FileNotFoundError(root)
    selected = sorted(paths if paths is not None else root.rglob("*.md"))
    entries: list[ChapterEntry] = []
    for path in selected:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        entries.append(ChapterEntry(
            path=path.relative_to(root).as_posix(),
            title=chapter_title(text, path.stem),
            bytes=path.stat().st_size,
            words=word_count(text),
            sections=section_count(text),
        ))
    return entries

def write_manifest(entries: Iterable[ChapterEntry], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = [entry.to_dict() for entry in sorted(entries, key=lambda item: item.path)]
    destination.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
