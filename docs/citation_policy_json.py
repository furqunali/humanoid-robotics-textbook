"""Stable JSON contract for citation policy findings."""
from __future__ import annotations
from dataclasses import asdict
import json
from docs.citation_policy import CitationFinding

def to_json(findings: tuple[CitationFinding, ...]) -> str:
    return json.dumps([asdict(finding) for finding in findings], sort_keys=True, separators=(",", ":"))
