import pytest

from docs.ingest_config import IngestConfig


def test_config_accepts_small_positive_vector_size():
    assert IngestConfig(collection_name="docs", vector_size=1).validate() is None

def test_config_rejects_zero_vector_size():
    with pytest.raises(ValueError):
        IngestConfig(collection_name="docs", vector_size=0).validate()

def test_config_rejects_negative_vector_size():
    with pytest.raises(ValueError):
        IngestConfig(collection_name="docs", vector_size=-1).validate()
