from docs.ingest_config import IngestConfig

def test_ingest_config_stores_collection_and_vector_size():
    config = IngestConfig(collection_name="robotics", vector_size=1536)
    assert config.collection_name == "robotics"
    assert config.vector_size == 1536

def test_ingest_config_accepts_positive_vector_size():
    config = IngestConfig(collection_name="docs", vector_size=1)
    assert config.vector_size == 1

def test_ingest_config_accepts_normal_http_collection_setup():
    config = IngestConfig(collection_name="docs", vector_size=768)
    assert config.validate() is None
