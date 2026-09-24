import pytest

from docs.reading_level import (
    ReadingLevel,
    analyze,
    count_syllables,
    grade_label,
    reading_ease,
)


def test_analyze_simple_sentence_known_score():
    result = analyze("The cat sat.")
    assert result.words == 3
    assert result.sentences == 1
    assert result.syllables == 3
    # 206.835 - 1.015*(3/1) - 84.6*(3/3) == 119.19
    assert result.score == 119.19


def test_analyze_returns_frozen_dataclass():
    result = analyze("Robots move.")
    assert isinstance(result, ReadingLevel)
    with pytest.raises(Exception):
        result.score = 1.0  # type: ignore[misc]


def test_empty_text_scores_zero():
    result = analyze("")
    assert result == ReadingLevel(words=0, sentences=0, syllables=0, score=0.0)


def test_text_with_no_words_scores_zero():
    assert analyze("!!! ... ???").score == 0.0


def test_missing_terminal_punctuation_counts_one_sentence():
    result = analyze("humanoid robotics is engaging")
    assert result.sentences == 1


def test_multiple_sentences_counted():
    result = analyze("Walk. Then run! Do you jump?")
    assert result.sentences == 3


def test_count_syllables_basic_words():
    assert count_syllables("cat") == 1
    assert count_syllables("robot") == 2
    assert count_syllables("humanoid") == 3


def test_count_syllables_drops_silent_e():
    assert count_syllables("make") == 1
    assert count_syllables("pose") == 1


def test_count_syllables_keeps_le_ending():
    assert count_syllables("able") == 2


def test_count_syllables_minimum_one():
    assert count_syllables("rhythm") >= 1


def test_count_syllables_ignores_non_alpha():
    assert count_syllables("42") == 0
    assert count_syllables("") == 0


def test_reading_ease_matches_analyze():
    text = "Actuators drive the joints of a walking robot."
    assert reading_ease(text) == analyze(text).score


def test_grade_label_boundaries():
    assert grade_label(90) == "very easy"
    assert grade_label(75) == "easy"
    assert grade_label(65) == "standard"
    assert grade_label(45) == "difficult"
    assert grade_label(10) == "very difficult"


def test_type_errors():
    with pytest.raises(TypeError):
        analyze(123)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        count_syllables(None)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        grade_label("high")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        grade_label(True)


def test_determinism():
    text = "The controller stabilizes the biped during dynamic locomotion."
    assert analyze(text) == analyze(text)
