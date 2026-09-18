import pytest
from docs.ingest_config import IngestConfig
from docs.ingest_schema import validate_ingest_config

def test_accepts_valid_ingest_config():
    assert validate_ingest_config(IngestConfig("https://qdrant.example.com","test-key")) is True

def test_rejects_invalid_vector_size():
    config = IngestConfig("https://qdrant.example.com","test-key",vector_size=0)
    with pytest.raises(ValueError, match="vector_size"):
        validate_ingest_config(config)
