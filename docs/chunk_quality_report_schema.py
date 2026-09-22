"""Schema validation for exported chunk-quality reports."""
from __future__ import annotations
REQUIRED_FIELDS = frozenset({"chunks","oversized","undersized","passed"})
def validate_chunk_quality_report(payload: dict) -> bool:
    if not isinstance(payload, dict) or set(payload) != REQUIRED_FIELDS: return False
    return isinstance(payload["passed"], bool) and all(
        type(payload[name]) is int and payload[name] >= 0 for name in ("chunks","oversized","undersized")
    )
