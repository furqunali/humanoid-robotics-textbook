from docs.knowledge_health import KnowledgeHealth
from docs.knowledge_health_json import to_json

def test_health_json_is_stable():
    health = KnowledgeHealth(4, 2, 100, 1.0, True)
    assert to_json(health) == '{"characters":100,"citation_coverage":1.0,"chunks":4,"healthy":true,"sources":2}'
