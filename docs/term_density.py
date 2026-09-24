"""Deterministic keyword/term density metrics for textbook passages.

Term density expresses how often a set of tracked terms appears relative to the
overall word count, reported as occurrences per 100 words. Matching is
case-insensitive and supports multi-word terms. All functions are pure.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")


def _tokenize(text: str) -> list[str]:
    return [match.lower() for match in _WORD_RE.findall(text)]


@dataclass(frozen=True)
class TermDensity:
    """Immutable density result for one tracked term.

    Attributes:
        term: The tracked term in its normalized (lower-case) form.
        occurrences: Number of times the term appears as a token sequence.
        density: Occurrences per 100 words, rounded to two decimals.
    """

    term: str
    occurrences: int
    density: float


def _normalize_terms(terms: list[str]) -> list[tuple[str, tuple[str, ...]]]:
    if not isinstance(terms, list):
        raise TypeError("terms must be a list of strings")
    normalized: list[tuple[str, tuple[str, ...]]] = []
    for term in terms:
        if not isinstance(term, str):
            raise TypeError("each term must be a string")
        tokens = tuple(_tokenize(term))
        if not tokens:
            raise ValueError("terms must contain at least one word character")
        normalized.append((" ".join(tokens), tokens))
    return normalized


def _count_occurrences(tokens: list[str], needle: tuple[str, ...]) -> int:
    span = len(needle)
    if span == 0 or span > len(tokens):
        return 0
    count = 0
    for start in range(len(tokens) - span + 1):
        if tuple(tokens[start:start + span]) == needle:
            count += 1
    return count


def analyze(text: str, terms: list[str]) -> tuple[TermDensity, ...]:
    """Compute per-term density for ``text``.

    Args:
        text: The passage to scan.
        terms: Terms to track; each may contain multiple words. Matching is
            case-insensitive. Duplicate terms are collapsed to their first
            occurrence order.

    Returns:
        A tuple of :class:`TermDensity` results in the order the terms were
        first supplied.

    Raises:
        TypeError: If ``text`` is not a string or ``terms`` is malformed.
        ValueError: If any term has no word characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    normalized = _normalize_terms(terms)
    tokens = _tokenize(text)
    total_words = len(tokens)
    results: list[TermDensity] = []
    seen: set[str] = set()
    for key, needle in normalized:
        if key in seen:
            continue
        seen.add(key)
        occurrences = _count_occurrences(tokens, needle)
        density = round(occurrences / total_words * 100, 2) if total_words else 0.0
        results.append(TermDensity(term=key, occurrences=occurrences, density=density))
    return tuple(results)


def total_word_count(text: str) -> int:
    """Return the number of word tokens in ``text``.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(_tokenize(text))


def dominant_term(text: str, terms: list[str]) -> TermDensity | None:
    """Return the single densest term, or ``None`` when nothing matches.

    Ties are broken by the order in which the terms were supplied, so the
    result is fully deterministic.
    """
    results = analyze(text, terms)
    best: TermDensity | None = None
    for result in results:
        if result.occurrences == 0:
            continue
        if best is None or result.density > best.density:
            best = result
    return best
