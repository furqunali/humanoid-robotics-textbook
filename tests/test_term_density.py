import pytest

from docs.term_density import (
    TermDensity,
    analyze,
    dominant_term,
    total_word_count,
)


def test_single_term_density():
    text = "robot robot arm servo"  # 4 words, robot appears twice
    (result,) = analyze(text, ["robot"])
    assert result.term == "robot"
    assert result.occurrences == 2
    assert result.density == 50.0


def test_case_insensitive_matching():
    (result,) = analyze("Robot ROBOT robot", ["robot"])
    assert result.occurrences == 3


def test_multi_word_term():
    text = "the control loop tightens the control loop again"
    (result,) = analyze(text, ["control loop"])
    assert result.occurrences == 2


def test_multiple_terms_preserve_order():
    results = analyze("servo motor servo joint", ["joint", "servo"])
    assert [r.term for r in results] == ["joint", "servo"]
    assert results[0].occurrences == 1
    assert results[1].occurrences == 2


def test_duplicate_terms_collapsed():
    results = analyze("gain gain", ["gain", "gain"])
    assert len(results) == 1
    assert results[0].occurrences == 2


def test_zero_occurrences():
    (result,) = analyze("no matching words here", ["quaternion"])
    assert result.occurrences == 0
    assert result.density == 0.0


def test_empty_text_density_zero():
    (result,) = analyze("", ["robot"])
    assert result.occurrences == 0
    assert result.density == 0.0


def test_total_word_count():
    assert total_word_count("one two three") == 3
    assert total_word_count("") == 0


def test_result_is_frozen_dataclass():
    (result,) = analyze("robot", ["robot"])
    assert isinstance(result, TermDensity)
    with pytest.raises(Exception):
        result.density = 0.0  # type: ignore[misc]


def test_dominant_term_picks_densest():
    text = "servo servo servo motor"
    best = dominant_term(text, ["motor", "servo"])
    assert best is not None
    assert best.term == "servo"


def test_dominant_term_none_when_no_match():
    assert dominant_term("empty of targets", ["torque"]) is None


def test_term_normalized_to_lower():
    (result,) = analyze("Torque torque", ["Torque"])
    assert result.term == "torque"
    assert result.occurrences == 2


def test_type_and_value_errors():
    with pytest.raises(TypeError):
        analyze(123, ["x"])  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        analyze("text", "notalist")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        analyze("text", [123])  # type: ignore[list-item]
    with pytest.raises(ValueError):
        analyze("text", ["   "])


def test_determinism():
    text = "gait gait balance gait balance"
    assert analyze(text, ["gait", "balance"]) == analyze(text, ["gait", "balance"])
