from docs.chunk_quality_report_schema import validate_chunk_quality_report


def _valid_report() -> dict:
    return {"chunks": 4, "oversized": 0, "undersized": 0, "passed": True}


def test_schema_rejects_bool_as_count():
    payload = _valid_report()
    payload["oversized"] = False
    assert not validate_chunk_quality_report(payload)


def test_schema_accepts_zero_counts():
    assert validate_chunk_quality_report(_valid_report())
