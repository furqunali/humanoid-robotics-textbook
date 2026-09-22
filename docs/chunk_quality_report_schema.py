"""Schema validation for exported chunk-quality reports."""
from __future__ import annotations

REQUIRED_FIELDS = frozenset({"chunks","oversized","undersized","passed"})
def validate_chunk_quality_report(payload: dict) -> bool:
    if not isinstance(payload, dict) or set(payload) != REQUIRED_FIELDS: return False
    counts = ("chunks","oversized","undersized")
    if not all(type(payload[name]) is int and payload[name] >= 0 for name in counts): return False
    if not isinstance(payload["passed"], bool): return False
    return payload["oversized"] + payload["undersized"] <= payload["chunks"] and payload["passed"] == (
        payload["oversized"] == 0 and payload["undersized"] == 0
    )
