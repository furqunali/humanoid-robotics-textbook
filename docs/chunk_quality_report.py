"""Stable JSON export for textbook chunk-quality gates."""
from __future__ import annotations
import json
from dataclasses import asdict
from .chunk_quality_gate import ChunkQualityGate

def chunk_quality_report_dict(result: ChunkQualityGate) -> dict:
    if not isinstance(result, ChunkQualityGate):
        raise TypeError("result must be a ChunkQualityGate")
    return asdict(result)

def chunk_quality_report_json(result: ChunkQualityGate) -> str:
    return json.dumps(chunk_quality_report_dict(result), sort_keys=True)
