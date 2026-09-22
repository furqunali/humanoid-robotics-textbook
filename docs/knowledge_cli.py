"""Small CLI helpers for reproducible textbook knowledge exports."""
from __future__ import annotations

import argparse
from pathlib import Path

from docs.knowledge_source import build_knowledge_source, write_jsonl


def export_knowledge(root: Path, destination: Path, max_chars: int = 1200) -> int:
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    chunks = build_knowledge_source(root, max_chars=max_chars)
    write_jsonl(chunks, destination)
    return len(chunks)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export citation-ready textbook knowledge")
    parser.add_argument("root", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--max-chars", type=int, default=1200)
    return parser

def main() -> int:
    args = build_parser().parse_args()
    count = export_knowledge(args.root, args.destination, args.max_chars)
    print(f"exported_chunks={count}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
