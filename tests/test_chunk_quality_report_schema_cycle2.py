from docs.chunk_quality_report_schema import validate_chunk_quality_report


def test_chunk_report_rejects_overlapping_counts():
    payload = {"chunks": 3, "oversized": 2, "undersized": 2, "passed": False}
    assert not validate_chunk_quality_report(payload)

def test_chunk_report_rejects_passed_with_quality_issues():
    payload = {"chunks": 3, "oversized": 1, "undersized": 0, "passed": True}
    assert not validate_chunk_quality_report(payload)

def test_chunk_report_rejects_negative_counts():
    payload = {"chunks": -1, "oversized": 0, "undersized": 0, "passed": True}
    assert not validate_chunk_quality_report(payload)
