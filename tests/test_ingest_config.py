import pytest

from docs.ingest_config import load_config


def test_rejects_invalid_qdrant_url(monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "not-a-url")
    monkeypatch.setenv("QDRANT_API_KEY", "test-key")
    with pytest.raises(ValueError, match="valid HTTP"):
        load_config()


def test_loads_valid_configuration(monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "https://qdrant.example.com")
    monkeypatch.setenv("QDRANT_API_KEY", "test-key")
    config = load_config()
    assert config.qdrant_url == "https://qdrant.example.com"
    assert config.collection_name == "robotics_textbook"
    assert config.vector_size == 1536


def test_loads_custom_collection_and_vector_size(monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "https://qdrant.example.com")
    monkeypatch.setenv("QDRANT_API_KEY", "test-key")
    monkeypatch.setenv("QDRANT_COLLECTION", "robotics_v2")
    monkeypatch.setenv("QDRANT_VECTOR_SIZE", "768")

    config = load_config()

    assert config.collection_name == "robotics_v2"
    assert config.vector_size == 768


@pytest.mark.parametrize(
    ("name", "value", "message"),
    [
        ("QDRANT_COLLECTION", "", "must not be empty"),
        ("QDRANT_VECTOR_SIZE", "not-an-int", "must be an integer"),
        ("QDRANT_VECTOR_SIZE", "0", "must be positive"),
    ],
)
def test_rejects_invalid_optional_config(monkeypatch, name, value, message):
    monkeypatch.setenv("QDRANT_URL", "https://qdrant.example.com")
    monkeypatch.setenv("QDRANT_API_KEY", "test-key")
    monkeypatch.setenv(name, value)

    with pytest.raises(ValueError, match=message):
        load_config()


def test_validate_source_url_accepts_https():
    from docs.ingest_config import validate_source_url
    assert validate_source_url(" https://example.com/textbook ") == "https://example.com/textbook"


def test_validate_source_url_rejects_non_http():
    from docs.ingest_config import validate_source_url
    with pytest.raises(ValueError, match="HTTP\(S\)"):
        validate_source_url("ftp://example.com/textbook")
