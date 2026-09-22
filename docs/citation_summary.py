"""Aggregate deterministic citation policy findings."""
from __future__ import annotations
from dataclasses import dataclass
from docs.citation_policy import CitationFinding

@dataclass(frozen=True)
class CitationSummary:
    total: int
    errors: int
    warnings: int
    infos: int
    covered: bool

def summarize_citations(findings: tuple[CitationFinding, ...]) -> CitationSummary:
    errors = sum(f.severity == "error" for f in findings)
    warnings = sum(f.severity == "warning" for f in findings)
    infos = sum(f.severity == "info" for f in findings)
    return CitationSummary(len(findings), errors, warnings, infos, errors == 0)
