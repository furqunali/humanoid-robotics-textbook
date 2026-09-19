import pytest

from docs.ingest_config import IngestConfig, validate_http_url, validate_source_url


def test_validate_http_url_accepts_https():
    assert validate_http_url("https://example.com/file.pdf") == "https://example.com/file.pdf"


def test_validate_http_url_accepts_http():
    assert validate_http_url("http://example.com/file.pdf") == "http://example.com/file.pdf"


def test_validate_http_url_rejects_missing_scheme():
    with pytest.raises(ValueError):
        validate_http_url("example.com/file.pdf")


def test_validate_http_url_rejects_embedded_credentials():
    with pytest.raises(ValueError):
        validate_http_url("https://user:pass@example.com/file.pdf")


def test_config_validation_rejects_non_positive_vector_size():
    config = IngestConfig(collection_name="docs", vector_size=0)
    with pytest.raises(ValueError, match="positive"):
        config.validate()
