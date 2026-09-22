import pytest

from docs.ingest_validation import validate_source_label, validate_source_scheme


def test_source_label_preserves_internal_spacing():
    assert validate_source_label("  lecture   notes  ") == "lecture   notes"

def test_source_label_accepts_maximum_length():
    value = "x" * 200
    assert validate_source_label(value) == value

def test_source_label_rejects_empty_none():
    with pytest.raises(ValueError):
        validate_source_label(None)

def test_scheme_normalizes_mixed_case():
    assert validate_source_scheme("HTTPS://example.com") == "https"

def test_scheme_rejects_empty_value():
    with pytest.raises(ValueError):
        validate_source_scheme("")
