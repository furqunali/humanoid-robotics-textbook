import pytest

from docs.ingest_defaults import (
    DEFAULT_COLLECTION,
    DEFAULT_VECTOR_SIZE,
    normalize_collection_name,
    parse_vector_size,
)


def test_normalize_collection_name_keeps_hyphens_and_underscores():
    assert normalize_collection_name(" robotics_textbook-v2 ") == "robotics_textbook-v2"


def test_normalize_collection_name_defaults_when_value_is_none():
    assert normalize_collection_name(None) == DEFAULT_COLLECTION


def test_parse_vector_size_accepts_large_positive_values():
    assert parse_vector_size("4096") == 4096


def test_parse_vector_size_strips_whitespace_before_parsing():
    assert parse_vector_size(" 1536 ") == DEFAULT_VECTOR_SIZE


def test_parse_vector_size_rejects_decimal_text():
    with pytest.raises(ValueError, match="must be an integer"):
        parse_vector_size("1536.0")
