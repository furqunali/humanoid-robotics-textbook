"""Provision the Qdrant collection used by the textbook ingestion pipeline.

Credentials are supplied through environment variables so secrets are never
stored in source control.
"""

from __future__ import annotations

import os

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

COLLECTION_NAME = "robotics_textbook"
VECTOR_SIZE = 1536


def build_client() -> QdrantClient:
    """Build a Qdrant client from the runtime environment."""
    url = os.environ.get("QDRANT_URL")
    api_key = os.environ.get("QDRANT_API_KEY")
    if not url:
        raise RuntimeError("QDRANT_URL is required")
    if not api_key:
        raise RuntimeError("QDRANT_API_KEY is required")
    return QdrantClient(url=url, api_key=api_key)


def setup_db(client: QdrantClient) -> None:
    """Create the textbook collection with the configured vector schema."""
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
    )


if __name__ == "__main__":
    setup_db(build_client())
