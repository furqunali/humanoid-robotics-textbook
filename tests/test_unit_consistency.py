import pytest

from docs.unit_consistency import (
    UnitConflict,
    find_conflicts,
    is_consistent,
    known_quantities,
    variants_used,
)


def test_length_conflict_m_and_meter():
    (conflict,) = find_conflicts("The link is 2 m long, roughly two meters.")
    assert conflict.quantity == "length"
    assert conflict.variants == ("m", "meter")


def test_time_conflict_s_and_sec():
    (conflict,) = find_conflicts("Sample every 1 s, i.e. once per sec.")
    assert conflict.quantity == "time"
    assert conflict.variants == ("s", "sec")


def test_angle_conflict_rad_and_radian():
    (conflict,) = find_conflicts("Rotate 1 rad, about one radian.")
    assert conflict.quantity == "angle"
    assert conflict.variants == ("rad", "radian")


def test_consistent_when_single_variant():
    assert is_consistent("The joint travels 3 m before the stop.")
    assert find_conflicts("The joint travels 3 m before the stop.") == ()


def test_consistent_with_only_word_form():
    assert is_consistent("It weighs several kilograms in total.")


def test_single_letter_not_matched_inside_word():
    # "meters" must not trigger the bare "m" symbol variant on its own.
    assert is_consistent("The distance is several meters overall.")


def test_multiple_conflicts_sorted_by_quantity():
    text = "Move 2 m and two meters in 1 s over one second."
    conflicts = find_conflicts(text)
    assert [c.quantity for c in conflicts] == ["length", "time"]


def test_force_symbol_case_sensitive():
    # "N" (newton) plus the word "newton" is a conflict.
    (conflict,) = find_conflicts("Apply 5 N, i.e. five newtons.")
    assert conflict.quantity == "force"
    assert conflict.variants == ("N", "newton")


def test_variants_used_reports_present_units():
    usage = variants_used("Set torque and move 4 m and two meters.")
    assert usage["length"] == ("m", "meter")
    assert "time" not in usage


def test_variants_used_empty_when_no_units():
    assert variants_used("no units mentioned in this line") == {}


def test_three_time_variants_all_reported():
    conflict = find_conflicts("1 s equals one sec equals one second")[0]
    assert conflict.variants == ("s", "sec", "second")


def test_conflict_is_frozen_dataclass():
    (conflict,) = find_conflicts("2 m and two meters")
    assert isinstance(conflict, UnitConflict)
    with pytest.raises(Exception):
        conflict.quantity = "time"  # type: ignore[misc]


def test_known_quantities_sorted():
    quantities = known_quantities()
    assert quantities == tuple(sorted(quantities))
    assert "length" in quantities and "force" in quantities


def test_type_errors():
    with pytest.raises(TypeError):
        find_conflicts(123)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        variants_used(None)  # type: ignore[arg-type]


def test_determinism():
    text = "3 m and three meters at 2 s and two seconds"
    assert find_conflicts(text) == find_conflicts(text)
