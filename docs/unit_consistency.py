"""Flag inconsistent SI unit spelling for robotics quantities.

Textbook prose often mixes an abbreviated unit with its spelled-out form (for
example ``m`` and ``meter``, or ``s`` and ``sec``). This module detects, per
physical quantity, when more than one spelling variant of the same unit is
used, so an editor can standardize on one form. Detection is deterministic.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

# Each quantity maps a canonical variant name to the set of surface spellings
# that denote the *same* unit. A quantity is inconsistent when two or more of
# its variants appear in the text.
_UNIT_GROUPS: dict[str, dict[str, tuple[str, ...]]] = {
    "length": {
        "m": ("m",),
        "meter": ("meter", "meters", "metre", "metres"),
    },
    "time": {
        "s": ("s",),
        "sec": ("sec", "secs"),
        "second": ("second", "seconds"),
    },
    "angle": {
        "rad": ("rad",),
        "radian": ("radian", "radians"),
    },
    "mass": {
        "kg": ("kg",),
        "kilogram": ("kilogram", "kilograms"),
    },
    "force": {
        "N": ("N",),
        "newton": ("newton", "newtons"),
    },
}


@dataclass(frozen=True)
class UnitConflict:
    """An inconsistent unit usage for a single physical quantity.

    Attributes:
        quantity: The physical quantity, e.g. ``"length"`` or ``"time"``.
        variants: The distinct spelling variants found, sorted alphabetically.
    """

    quantity: str
    variants: tuple[str, ...]


def _variant_pattern(spellings: tuple[str, ...]) -> re.Pattern[str]:
    # Sort longest-first so "meters" is preferred over "meter" during matching.
    alternatives = sorted((re.escape(s) for s in spellings), key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z])(?:" + "|".join(alternatives) + r")(?![A-Za-z])")


# Precompiled patterns keep repeated scans deterministic and cheap.
_COMPILED: dict[str, dict[str, re.Pattern[str]]] = {
    quantity: {variant: _variant_pattern(spellings) for variant, spellings in variants.items()}
    for quantity, variants in _UNIT_GROUPS.items()
}


def _found_variants(text: str, quantity: str) -> tuple[str, ...]:
    found = [
        variant
        for variant, pattern in _COMPILED[quantity].items()
        if pattern.search(text) is not None
    ]
    return tuple(sorted(found))


def find_conflicts(text: str) -> tuple[UnitConflict, ...]:
    """Return the quantities whose unit spelling is inconsistent.

    A quantity is reported only when two or more distinct spelling variants of
    the same unit appear in ``text``. Case matters for single-letter symbols
    (``N`` the newton is distinguished from stray lowercase ``n``); word forms
    match case-insensitively via their lower-case spellings.

    Args:
        text: The prose to scan.

    Returns:
        A tuple of :class:`UnitConflict` values ordered by quantity name.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    conflicts: list[UnitConflict] = []
    for quantity in sorted(_UNIT_GROUPS):
        variants = _found_variants(text, quantity)
        if len(variants) >= 2:
            conflicts.append(UnitConflict(quantity=quantity, variants=variants))
    return tuple(conflicts)


def is_consistent(text: str) -> bool:
    """Return ``True`` when no quantity mixes unit spellings in ``text``."""
    return len(find_conflicts(text)) == 0


def variants_used(text: str) -> dict[str, tuple[str, ...]]:
    """Return every quantity mapped to the spelling variants it uses.

    Quantities with no variants present are omitted, keeping the result
    focused on units the text actually mentions.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    usage: dict[str, tuple[str, ...]] = {}
    for quantity in sorted(_UNIT_GROUPS):
        variants = _found_variants(text, quantity)
        if variants:
            usage[quantity] = variants
    return usage


def known_quantities() -> tuple[str, ...]:
    """Return the physical quantities this module can check, sorted by name."""
    return tuple(sorted(_UNIT_GROUPS))
