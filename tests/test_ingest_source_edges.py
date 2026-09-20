import pytest
from docs.ingest_validation import validate_source_label, validate_source_scheme

def test_source_label_strips_outer_newlines():
    assert validate_source_label("\\nlecture notes\\n") == "lecture notes"

def test_source_label_accepts_single_character():
    assert validate_source_label("x") == "x"

def test_source_label_rejects_201_characters():
    with pytest.raises(ValueError):
        validate_source_label("x" * 201)

def test_source_scheme_is_lowercase():
    assert validate_source_scheme("HTTP://example.com") == "http"

def test_source_scheme_rejects_ftp():
    with pytest.raises(ValueError):
        validate_source_scheme("ftp://example.com")
