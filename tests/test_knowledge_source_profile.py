from docs.knowledge_source import KnowledgeChunk
from docs.knowledge_source_profile import profile_source_lengths


def c(i,s,t): return KnowledgeChunk(str(i),s,"title",t,i)

def test_profiles_each_source():
    result=profile_source_lengths([c(0,"a","abc"),c(1,"a","abcdef"),c(2,"b","xy")])
    assert result[0].minimum == 3 and result[0].maximum == 6
    assert result[0].average == 4.5 and result[1].chunks == 1

def test_empty_is_empty():
    assert profile_source_lengths([]) == ()
