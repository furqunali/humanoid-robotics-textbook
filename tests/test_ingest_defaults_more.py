import pytest
from docs.ingest_defaults import parse_vector_size, normalize_collection_name

def test_collection_name_strips_tabs():
    assert normalize_collection_name("\\t robotics \\t") == "robotics"

def test_collection_name_empty_uses_default():
    assert normalize_collection_name("") == "robotics_textbook"

def test_vector_size_empty_uses_default():
    assert parse_vector_size("") == 1536

def test_vector_size_rejects_zero():
    with pytest.raises(ValueError):
        parse_vector_size("0")

def test_vector_size_rejects_negative():
    with pytest.raises(ValueError):
        parse_vector_size("-1")
