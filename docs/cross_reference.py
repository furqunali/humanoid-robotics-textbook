"""Detect chapter and section cross-references inside textbook prose.

The scanner recognizes references such as ``Chapter 3``, ``see Section 2.1``,
``Appendix B``, and ``Figure 4`` and returns them in reading order. Detection
is deterministic and depends only on the supplied text.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

# Ordered so the compiled pattern reports the reference kind via named groups.
_REFERENCE_RE = re.compile(
    r"\b(?:"
    r"(?P<chapter>chapters?)\s+(?P<chapter_id>\d+(?:\.\d+)*)"
    r"|(?P<section>sections?)\s+(?P<section_id>\d+(?:\.\d+)*)"
    r"|(?P<appendix>appendix)\s+(?P<appendix_id>[A-Z]\b|\d+)"
    r"|(?P<figure>figures?)\s+(?P<figure_id>\d+(?:\.\d+)*)"
    r"|(?P<table>tables?)\s+(?P<table_id>\d+(?:\.\d+)*)"
    r")",
    re.IGNORECASE,
)

_KINDS = ("chapter", "section", "appendix", "figure", "table")


@dataclass(frozen=True)
class CrossReference:
    """A single cross-reference discovered in text.

    Attributes:
        kind: One of ``"chapter"``, ``"section"``, ``"appendix"``,
            ``"figure"``, or ``"table"``.
        identifier: The referenced label, e.g. ``"3"``, ``"2.1"``, or ``"B"``.
        start: Character offset where the reference begins.
    """

    kind: str
    identifier: str
    start: int

    @property
    def label(self) -> str:
        """Human-readable label such as ``"Chapter 3"``."""
        return f"{self.kind.capitalize()} {self.identifier}"


def find_references(text: str) -> tuple[CrossReference, ...]:
    """Return every cross-reference in ``text`` in reading order.

    Args:
        text: The prose to scan.

    Returns:
        A tuple of :class:`CrossReference` values ordered by position.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    found: list[CrossReference] = []
    for match in _REFERENCE_RE.finditer(text):
        for kind in _KINDS:
            if match.group(kind):
                identifier = match.group(f"{kind}_id")
                # Normalize a single-letter appendix id to upper case.
                if kind == "appendix" and identifier.isalpha():
                    identifier = identifier.upper()
                found.append(
                    CrossReference(kind=kind, identifier=identifier, start=match.start())
                )
                break
    return tuple(found)


def referenced_labels(text: str) -> tuple[str, ...]:
    """Return the unique reference labels in first-seen order."""
    seen: dict[str, None] = {}
    for reference in find_references(text):
        seen.setdefault(reference.label, None)
    return tuple(seen.keys())


def reference_counts(text: str) -> dict[str, int]:
    """Return a mapping of reference kind to the number of matches found.

    Every recognized kind is present in the result, even when its count is
    zero, so callers can rely on a stable set of keys.
    """
    counts = {kind: 0 for kind in _KINDS}
    for reference in find_references(text):
        counts[reference.kind] += 1
    return counts
