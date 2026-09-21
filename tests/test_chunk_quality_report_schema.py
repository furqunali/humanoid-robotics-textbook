from docs.chunk_quality_report_schema import validate_chunk_quality_report

def test_valid_chunk_schema():
    assert validate_chunk_quality_report({"chunks":4,"oversized":1,"undersized":0,"passed":False})

def test_missing_field_fails():
    assert not validate_chunk_quality_report({"chunks":4,"oversized":1,"undersized":0})
