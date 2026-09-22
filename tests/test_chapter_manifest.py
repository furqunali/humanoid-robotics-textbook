from pathlib import Path

from docs.chapter_manifest import (
    build_manifest,
    chapter_title,
    section_count,
    write_manifest,
)


def test_manifest_collects_stable_metadata(tmp_path: Path):
    chapter = tmp_path / "intro.md"
    chapter.write_text("# Introduction\n\n## Setup\nWords here.", encoding="utf-8")
    entries = build_manifest(tmp_path)
    assert len(entries) == 1
    assert entries[0].title == "Introduction"
    assert entries[0].sections == 1
    assert entries[0].words == 5


def test_title_and_section_fallbacks():
    assert chapter_title("No heading", "fallback") == "fallback"
    assert section_count("# Main\ntext") == 0


def test_manifest_writer_is_json(tmp_path: Path):
    chapter = tmp_path / "z.md"
    chapter.write_text("# Z", encoding="utf-8")
    destination = tmp_path / "manifest.json"
    write_manifest(build_manifest(tmp_path), destination)
    assert '"path": "z.md"' in destination.read_text(encoding="utf-8")
