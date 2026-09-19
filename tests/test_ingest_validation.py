import pytest

from docs.ingest_validation import validate_source_label, validate_source_scheme


def test_validate_source_label_strips_whitespace():
    assert validate_source_label("  lecture notes  ") == "lecture notes"


def test_validate_source_label_rejects_empty_values():
    with pytest.raises(ValueError, match="must not be empty"):
        validate_source_label("   ")


def test_validate_source_label_rejects_overlong_values():
    with pytest.raises(ValueError, match="200 characters"):
        validate_source_label("x" * 201)


def test_validate_source_scheme_accepts_http_and_https():
    assert validate_source_scheme("https://example.com/chapter") == "https"
    assert validate_source_scheme("http://example.com/chapter") == "http"


def test_validate_source_scheme_rejects_other_schemes():
    with pytest.raises(ValueError, match="http/https"):
        validate_source_scheme("ftp://example.com/chapter")
