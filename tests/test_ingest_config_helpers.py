import pytest

from docs.ingest_config import validate_http_url


def test_validate_http_url_accepts_https():
    assert validate_http_url("https://example.com/source") == "https://example.com/source"


def test_validate_http_url_accepts_http():
    assert validate_http_url("http://example.com/source") == "http://example.com/source"


def test_validate_http_url_rejects_non_http_scheme():
    with pytest.raises(ValueError, match="http"):
        validate_http_url("ftp://example.com/source")


def test_validate_http_url_rejects_embedded_credentials():
    with pytest.raises(ValueError, match="credentials"):
        validate_http_url("https://user:pass@example.com/source")
