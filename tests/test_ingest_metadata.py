from docs.ingest_metadata import validate_metadata

def test_validate_metadata_normalizes_fields():
    item = validate_metadata(" docs/a.md ", "  Humanoid Robotics ", "  locomotion ")
    assert item.source == "docs/a.md"
    assert item.title == "Humanoid Robotics"
    assert item.section == "locomotion"

def test_validate_metadata_rejects_blank_fields():
    import pytest
    with pytest.raises(ValueError):
        validate_metadata("docs/a.md", "", "intro")
