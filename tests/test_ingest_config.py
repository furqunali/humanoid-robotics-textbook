from __future__ import annotations

import pytest

from docs.ingest_config import load_config


def test_load_config_requires_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("QDRANT_URL", raising=False)
    monkeypatch.delenv("QDRANT_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="QDRANT_URL"):
        load_config()


def test_load_config_reads_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("QDRANT_URL", "https://example.invalid")
    monkeypatch.setenv("QDRANT_API_KEY", "test-key")

    config = load_config()

    assert config.qdrant_url == "https://example.invalid"
    assert config.qdrant_api_key == "test-key"
    assert config.collection_name == "robotics_textbook"
    assert config.vector_size == 1536
