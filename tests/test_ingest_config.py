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


def test_validate_source_url_accepts_https():
    from docs.ingest_config import validate_source_url
    assert validate_source_url(" https://example.com/textbook ") == "https://example.com/textbook"


def test_validate_source_url_rejects_non_http():
    from docs.ingest_config import validate_source_url
    import pytest
    with pytest.raises(ValueError, match="HTTP\(S\)"):
        validate_source_url("ftp://example.com/textbook")
