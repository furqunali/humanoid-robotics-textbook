"""Stable JSON contract for citation policy findings."""
from __future__ import annotations

import json
from dataclasses import asdict

from docs.citation_policy import CitationFinding


def to_json(findings: tuple[CitationFinding, ...]) -> str:
    return json.dumps([asdict(finding) for finding in findings], sort_keys=True, separators=(",", ":"))
