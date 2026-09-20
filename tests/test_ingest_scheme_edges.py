import pytest
from docs.ingest_validation import validate_source_scheme

def test_scheme_accepts_uppercase_https():
    assert validate_source_scheme("HTTPS://example.com") == "https"

def test_scheme_accepts_mixed_case_http():
    assert validate_source_scheme("Http://example.com") == "http"

def test_scheme_rejects_file_scheme():
    with pytest.raises(ValueError):
        validate_source_scheme("file:///tmp/book.pdf")

def test_scheme_rejects_missing_scheme():
    with pytest.raises(ValueError):
        validate_source_scheme("example.com")
