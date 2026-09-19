import pytest

from docs.ingest_defaults import (
    DEFAULT_COLLECTION,
    DEFAULT_VECTOR_SIZE,
    normalize_collection_name,
    parse_vector_size,
)


def test_normalize_collection_name_strips_whitespace():
    assert normalize_collection_name("  robotics  ") == "robotics"


def test_normalize_collection_name_uses_default_for_blank():
    assert normalize_collection_name("   ") == DEFAULT_COLLECTION
    assert normalize_collection_name(None) == DEFAULT_COLLECTION


def test_parse_vector_size_uses_default_for_blank():
    assert parse_vector_size("") == DEFAULT_VECTOR_SIZE
    assert parse_vector_size(None) == DEFAULT_VECTOR_SIZE


def test_parse_vector_size_accepts_positive_integer():
    assert parse_vector_size(" 2048 ") == 2048


def test_parse_vector_size_rejects_non_integer():
    with pytest.raises(ValueError, match="must be an integer"):
        parse_vector_size("large")


def test_parse_vector_size_rejects_non_positive_integer():
    with pytest.raises(ValueError, match="must be positive"):
        parse_vector_size("0")
