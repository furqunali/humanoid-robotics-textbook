from pathlib import Path

import pytest

from docs.knowledge_search import (
    SearchIndex,
    SearchResult,
    build_search_index,
    tokenize,
    write_search_results,
)
from docs.knowledge_source import KnowledgeChunk


def chunk(cid: str, text: str, *, source: str = "chapters/intro.md",
          title: str = "Intro", index: int = 0) -> KnowledgeChunk:
    return KnowledgeChunk(cid, source, title, text, index)


CORPUS = [
    chunk("a", "A humanoid robot uses actuators to move each joint.",
          source="chapters/actuators.md", title="Actuators", index=0),
    chunk("b", "Bipedal balance keeps the humanoid upright while walking.",
          source="chapters/balance.md", title="Balance", index=0),
    chunk("c", "Sensors and actuators feed the control loop of a robot.",
          source="chapters/sensors.md", title="Sensors", index=0),
    chunk("d", "The vision pipeline detects obstacles for navigation.",
          source="chapters/vision.md", title="Vision", index=0),
]


def test_tokenize_is_lowercase_and_alphanumeric():
    assert tokenize("Humanoid-Robot's ACTUATORS!") == [
        "humanoid", "robot", "s", "actuators",
    ]
    assert tokenize("") == []


def test_tokenize_rejects_non_string():
    with pytest.raises(TypeError):
        tokenize(123)  # type: ignore[arg-type]


def test_search_ranks_relevant_chunk_first():
    index = build_search_index(CORPUS)
    results = index.search("actuators")
    assert results, "expected at least one hit for a corpus term"
    # 'actuators' appears in chapters a and c; both must rank above nothing else.
    ids = [r.chunk_id for r in results]
    assert set(ids) == {"a", "c"}
    assert all(r.score > 0 for r in results)


def test_search_only_returns_matching_chunks():
    index = build_search_index(CORPUS)
    results = index.search("vision obstacles navigation")
    assert [r.chunk_id for r in results] == ["d"]


def test_search_missing_term_returns_empty():
    index = build_search_index(CORPUS)
    assert index.search("submarine") == []


def test_empty_query_returns_empty():
    index = build_search_index(CORPUS)
    assert index.search("") == []
    assert index.search("   !!!   ") == []


def test_search_is_deterministic_regardless_of_input_order():
    forward = build_search_index(CORPUS)
    reverse = build_search_index(list(reversed(CORPUS)))
    a = forward.search("robot actuators")
    b = reverse.search("robot actuators")
    assert a == b
    # Duplicated call is identical too.
    assert forward.search("robot actuators") == a


def test_tie_break_is_stable_on_source_index_id():
    # Two chunks with identical text/length score identically for a shared
    # term; ordering must fall back to (source, index, chunk_id).
    tied = [
        chunk("z", "control loop feedback", source="chapters/zeta.md", index=1),
        chunk("y", "control loop feedback", source="chapters/alpha.md", index=0),
    ]
    index = build_search_index(tied)
    results = index.search("control loop feedback")
    assert [r.score for r in results][0] == [r.score for r in results][1]
    assert [r.chunk_id for r in results] == ["y", "z"]  # alpha#0 before zeta#1


def test_limit_caps_results_and_validates():
    index = build_search_index(CORPUS)
    # 'a' term matches actuators/balance/sensors chunks (they share letters?);
    # use a shared real term instead.
    results = index.search("robot", limit=1)
    assert len(results) == 1
    with pytest.raises(ValueError):
        index.search("robot", limit=0)
    with pytest.raises(ValueError):
        index.search("robot", limit=True)  # type: ignore[arg-type]


def test_idf_is_non_negative_for_ubiquitous_term():
    # 'shared' is in every document -> the +1-shifted BM25 idf stays strictly
    # non-negative (a classic un-shifted idf would go negative here).
    corpus = [
        chunk("1", "shared alpha", source="s/1.md", index=0),
        chunk("2", "shared beta", source="s/2.md", index=0),
        chunk("3", "shared gamma", source="s/3.md", index=0),
    ]
    index = build_search_index(corpus)
    assert index._idf("shared") >= 0.0
    # The ubiquitous term still matches every doc; identical scores fall back
    # to (source, index, id) ordering.
    ubiquitous = index.search("shared")
    assert [r.chunk_id for r in ubiquitous] == ["1", "2", "3"]
    assert len({r.score for r in ubiquitous}) == 1
    # A discriminating term retrieves only its single owner.
    assert [r.chunk_id for r in index.search("beta")] == ["2"]
    # An unknown term scores nothing.
    assert index.search("submarine") == []


def test_build_rejects_duplicate_ids():
    with pytest.raises(ValueError, match="duplicate"):
        build_search_index([chunk("same", "one"), chunk("same", "two",
                                                         source="s/other.md")])


def test_build_rejects_empty_fields_and_bad_type():
    with pytest.raises(ValueError):
        build_search_index([chunk("", "text")])
    with pytest.raises(TypeError):
        build_search_index(["not a chunk"])  # type: ignore[list-item]


def test_build_rejects_bad_precision():
    with pytest.raises(ValueError):
        build_search_index(CORPUS, precision=-1)


def test_empty_corpus_is_searchable_and_empty():
    index = build_search_index([])
    assert index.size == 0
    assert index.average_length == 0.0
    assert index.search("anything") == []


def test_index_json_is_canonical_and_stable():
    forward = build_search_index(CORPUS)
    reverse = build_search_index(list(reversed(CORPUS)))
    assert forward.to_json() == reverse.to_json()
    payload = forward.to_dict()
    assert payload["document_frequency"]["robot"] == 2
    # documents are stored in canonical (source, index, id) order
    sources = [d["source"] for d in payload["documents"]]
    assert sources == sorted(sources)


def test_write_search_results_is_deterministic(tmp_path: Path):
    index = build_search_index(CORPUS)
    results = index.search("actuators robot")
    destination = tmp_path / "results.jsonl"
    written = write_search_results(results, destination)
    assert written == len(results)
    lines = destination.read_text(encoding="utf-8").splitlines()
    assert len(lines) == len(results)
    assert '"chunk_id"' in lines[0]
    # Re-writing identical results yields byte-identical output.
    again = tmp_path / "again.jsonl"
    write_search_results(results, again)
    assert again.read_bytes() == destination.read_bytes()


def test_search_result_score_is_rounded_to_precision():
    index = build_search_index(CORPUS, precision=3)
    result = index.search("actuators")[0]
    assert isinstance(result, SearchResult)
    assert round(result.score, 3) == result.score


def test_index_is_immutable():
    index = build_search_index(CORPUS)
    assert isinstance(index, SearchIndex)
    with pytest.raises(Exception):
        index.average_length = 5.0  # type: ignore[misc]
