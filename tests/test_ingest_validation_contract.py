import pytest

from docs.ingest_validation import validate_source_label, validate_source_scheme


def test_validate_source_label_returns_normalized_value():
    assert validate_source_label("  Chapter 1  ") == "Chapter 1"


def test_validate_source_label_rejects_missing_value():
    with pytest.raises(ValueError, match="must not be empty"):
        validate_source_label("")


def test_validate_source_label_enforces_maximum_length():
    with pytest.raises(ValueError, match="200 characters"):
        validate_source_label("x" * 201)


def test_validate_source_scheme_normalizes_case():
    assert validate_source_scheme("HTTPS://example.com/doc") == "https"


def test_validate_source_scheme_rejects_unsupported_scheme():
    with pytest.raises(ValueError, match="HTTP or HTTPS"):
        validate_source_scheme("ftp://example.com/doc")
