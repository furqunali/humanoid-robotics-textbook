"""Deterministic Flesch reading-ease scoring for textbook passages.

The Flesch reading-ease score rates how easy a passage is to read on a scale
that typically runs from 0 (very difficult) to 100 (very easy). It is computed
purely from the passage text using a syllable-counting heuristic, so the result
is stable and free of wall-clock or random inputs.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

_WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
_SENTENCE_RE = re.compile(r"[.!?]+")
_VOWEL_GROUP_RE = re.compile(r"[aeiouy]+")


@dataclass(frozen=True)
class ReadingLevel:
    """Immutable summary of a passage's readability.

    Attributes:
        words: Number of word tokens found in the passage.
        sentences: Number of sentences (at least one when any word exists).
        syllables: Total estimated syllables across all words.
        score: Flesch reading-ease score rounded to two decimals.
    """

    words: int
    sentences: int
    syllables: int
    score: float


def count_syllables(word: str) -> int:
    """Estimate the syllable count of a single English word.

    The heuristic counts contiguous vowel groups, drops a common trailing
    silent ``e``, and guarantees at least one syllable for any alphabetic word.

    Args:
        word: A single word; non-alphabetic characters are ignored.

    Returns:
        The estimated number of syllables (``0`` for words with no letters).

    Raises:
        TypeError: If ``word`` is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    letters = "".join(ch for ch in word.lower() if ch.isalpha())
    if not letters:
        return 0
    groups = _VOWEL_GROUP_RE.findall(letters)
    count = len(groups)
    # Drop a silent trailing "e" (e.g. "make"), but never below one syllable.
    if letters.endswith("e") and not letters.endswith("le") and count > 1:
        count -= 1
    return max(1, count)


def analyze(text: str) -> ReadingLevel:
    """Compute the Flesch reading-ease score for a passage.

    Args:
        text: The passage to analyze.

    Returns:
        A :class:`ReadingLevel` with token counts and the rounded score. An
        empty or word-free passage yields a score of ``0.0``.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = _WORD_RE.findall(text)
    word_count = len(words)
    if word_count == 0:
        return ReadingLevel(words=0, sentences=0, syllables=0, score=0.0)
    # At least one sentence: a passage with words but no terminal punctuation
    # is still a single sentence.
    sentence_count = max(1, len(_SENTENCE_RE.findall(text)))
    syllable_count = sum(count_syllables(word) for word in words)
    score = (
        206.835
        - 1.015 * (word_count / sentence_count)
        - 84.6 * (syllable_count / word_count)
    )
    return ReadingLevel(
        words=word_count,
        sentences=sentence_count,
        syllables=syllable_count,
        score=round(score, 2),
    )


def reading_ease(text: str) -> float:
    """Return only the rounded Flesch reading-ease score for ``text``."""
    return analyze(text).score


def grade_label(score: float) -> str:
    """Map a reading-ease score to a coarse difficulty label.

    Args:
        score: A Flesch reading-ease score.

    Returns:
        One of ``"very easy"``, ``"easy"``, ``"standard"``, ``"difficult"``,
        or ``"very difficult"``.

    Raises:
        TypeError: If ``score`` is not a real number.
    """
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("score must be a real number")
    if score >= 80.0:
        return "very easy"
    if score >= 70.0:
        return "easy"
    if score >= 60.0:
        return "standard"
    if score >= 30.0:
        return "difficult"
    return "very difficult"
