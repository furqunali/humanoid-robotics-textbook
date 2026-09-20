"""Policy findings for textbook citation coverage."""
from __future__ import annotations
from dataclasses import dataclass
from docs.knowledge_health import KnowledgeHealth

@dataclass(frozen=True)
class CitationFinding:
    code: str
    severity: str
    message: str

def evaluate_citations(health: KnowledgeHealth) -> tuple[CitationFinding, ...]:
    findings: list[CitationFinding] = []
    if health.chunks == 0:
        findings.append(CitationFinding("NO_CHUNKS", "warning", "textbook export contains no chunks"))
    if health.citation_coverage < 1.0:
        findings.append(CitationFinding("INCOMPLETE_COVERAGE", "error", f"citation coverage is {health.citation_coverage:.4f}"))
    if health.healthy and not findings:
        findings.append(CitationFinding("HEALTHY", "info", "citation coverage passed all health checks"))
    return tuple(findings)
