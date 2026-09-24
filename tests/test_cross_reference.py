import pytest

from docs.cross_reference import (
    CrossReference,
    find_references,
    reference_counts,
    referenced_labels,
)


def test_detects_chapter_reference():
    (ref,) = find_references("As shown in Chapter 3, gait matters.")
    assert ref.kind == "chapter"
    assert ref.identifier == "3"
    assert ref.label == "Chapter 3"


def test_detects_see_section_with_dotted_id():
    (ref,) = find_references("see Section 2.1 for details")
    assert ref.kind == "section"
    assert ref.identifier == "2.1"


def test_detects_appendix_letter_uppercased():
    (ref,) = find_references("refer to appendix b")
    assert ref.kind == "appendix"
    assert ref.identifier == "B"


def test_detects_figure_and_table():
    refs = find_references("Figure 4 and Table 2 illustrate the torque.")
    kinds = {r.kind for r in refs}
    assert kinds == {"figure", "table"}


def test_references_in_reading_order():
    text = "First see Section 5, then Chapter 1, finally Figure 9."
    refs = find_references(text)
    assert [r.kind for r in refs] == ["section", "chapter", "figure"]
    assert refs[0].start < refs[1].start < refs[2].start


def test_case_insensitive():
    (ref,) = find_references("CHAPTER 7 covers actuators")
    assert ref.kind == "chapter"
    assert ref.identifier == "7"


def test_plural_forms_matched():
    refs = find_references("Chapters 2 and Sections 3 are related")
    assert {r.kind for r in refs} == {"chapter", "section"}


def test_no_references_returns_empty():
    assert find_references("There are no references here.") == ()


def test_referenced_labels_unique_and_ordered():
    text = "Chapter 3, Chapter 3 again, and Section 1."
    assert referenced_labels(text) == ("Chapter 3", "Section 1")


def test_reference_counts_has_all_kinds():
    counts = reference_counts("Chapter 1 and Chapter 2 and Figure 5")
    assert counts["chapter"] == 2
    assert counts["figure"] == 1
    assert counts["section"] == 0
    assert set(counts) == {"chapter", "section", "appendix", "figure", "table"}


def test_result_is_frozen_dataclass():
    (ref,) = find_references("Chapter 1")
    assert isinstance(ref, CrossReference)
    with pytest.raises(Exception):
        ref.identifier = "9"  # type: ignore[misc]


def test_word_boundary_avoids_false_positive():
    # "Chapternote" should not match as a chapter reference.
    assert find_references("Chapternote 3 is not a reference") == ()


def test_type_error():
    with pytest.raises(TypeError):
        find_references(42)  # type: ignore[arg-type]


def test_determinism():
    text = "see Chapter 2 and Section 4.2 and Appendix C"
    assert find_references(text) == find_references(text)
