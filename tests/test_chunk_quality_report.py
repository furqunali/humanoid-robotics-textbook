from docs.chunk_quality_gate import ChunkQualityGate
from docs.chunk_quality_report import chunk_quality_report_dict, chunk_quality_report_json

def test_export_preserves_gate_fields():
    result = ChunkQualityGate(5, 1, 2, False)
    assert chunk_quality_report_dict(result) == {
        "chunks": 5, "oversized": 1, "undersized": 2, "passed": False
    }
    assert chunk_quality_report_json(result) == '{"chunks": 5, "oversized": 1, "passed": false, "undersized": 2}'


def test_export_rejects_wrong_type():
    try:
        chunk_quality_report_dict(None)
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError")


def test_export_enforces_schema():
    assert chunk_quality_report_dict(ChunkQualityGate(1, 0, 0, True))["chunks"] == 1
