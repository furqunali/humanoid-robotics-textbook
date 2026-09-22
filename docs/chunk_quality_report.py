"""Stable JSON export for textbook chunk-quality gates."""
from __future__ import annotations
import json
from dataclasses import asdict
from .chunk_quality_gate import ChunkQualityGate
from .chunk_quality_report_schema import validate_chunk_quality_report

def chunk_quality_report_dict(result: ChunkQualityGate) -> dict:
    if not isinstance(result, ChunkQualityGate):
        raise TypeError("result must be a ChunkQualityGate")
    payload = asdict(result)
    if not validate_chunk_quality_report(payload):
        raise ValueError("chunk quality report failed schema validation")
    return payload

def chunk_quality_report_json(result: ChunkQualityGate) -> str:
    return json.dumps(chunk_quality_report_dict(result), sort_keys=True)
