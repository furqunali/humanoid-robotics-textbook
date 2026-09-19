import pytest

from docs.ingest_config import load_config, validate_http_url


def test_validate_http_url_strips_whitespace():
    assert validate_http_url("  https://qdrant.example  ", "QDRANT_URL") == "https://qdrant.example"


def test_load_config_reads_environment(monkeypatch):
    monkeypatch.setenv("QDRANT_URL", " https://qdrant.example ")
    monkeypatch.setenv("QDRANT_API_KEY", " secret ")
    monkeypatch.setenv("QDRANT_COLLECTION", "robotics_docs")
    monkeypatch.setenv("QDRANT_VECTOR_SIZE", " 768 ")
    config = load_config()
    assert config.qdrant_url == "https://qdrant.example"
    assert config.qdrant_api_key == "secret"
    assert config.collection_name == "robotics_docs"
    assert config.vector_size == 768


def test_load_config_requires_credentials(monkeypatch):
    monkeypatch.delenv("QDRANT_URL", raising=False)
    monkeypatch.delenv("QDRANT_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="required"):
        load_config()


def test_load_config_rejects_invalid_collection(monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "https://qdrant.example")
    monkeypatch.setenv("QDRANT_API_KEY", "secret")
    monkeypatch.setenv("QDRANT_COLLECTION", "bad collection")
    with pytest.raises(ValueError, match="QDRANT_COLLECTION"):
        load_config()


def test_load_config_rejects_non_positive_vector_size(monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "https://qdrant.example")
    monkeypatch.setenv("QDRANT_API_KEY", "secret")
    monkeypatch.setenv("QDRANT_VECTOR_SIZE", "0")
    with pytest.raises(ValueError, match="must be positive"):
        load_config()
