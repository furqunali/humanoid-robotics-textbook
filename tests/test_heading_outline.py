import pytest

from docs.heading_outline import (
    OutlineNode,
    build_outline,
    flatten_titles,
    max_depth,
    parse_headings,
)


def test_single_heading():
    outline = build_outline("# Introduction")
    assert len(outline) == 1
    assert outline[0].level == 1
    assert outline[0].title == "Introduction"
    assert outline[0].children == ()


def test_nested_hierarchy():
    md = "# A\n## B\n### C\n## D"
    outline = build_outline(md)
    assert len(outline) == 1
    a = outline[0]
    assert [child.title for child in a.children] == ["B", "D"]
    assert a.children[0].children[0].title == "C"


def test_multiple_top_level_nodes():
    outline = build_outline("# One\n# Two")
    assert [node.title for node in outline] == ["One", "Two"]


def test_skipped_level_attaches_to_nearest_ancestor():
    outline = build_outline("# A\n### C")
    assert len(outline) == 1
    assert outline[0].children[0].level == 3
    assert outline[0].children[0].title == "C"


def test_ignores_headings_inside_code_fence():
    md = "# Real\n```\n# fake in code\n```\n## AlsoReal"
    titles = flatten_titles(build_outline(md))
    assert titles == ("Real", "AlsoReal")


def test_tilde_fence_ignored():
    md = "# Real\n~~~\n### fake\n~~~"
    assert flatten_titles(build_outline(md)) == ("Real",)


def test_trailing_hashes_stripped():
    (node,) = build_outline("## Title ##")
    assert node.title == "Title"


def test_parse_headings_flat_sequence():
    headings = parse_headings("# A\ntext\n## B")
    assert [(h.level, h.title) for h in headings] == [(1, "A"), (2, "B")]


def test_flatten_titles_depth_first_order():
    md = "# A\n## B\n### C\n# D"
    assert flatten_titles(build_outline(md)) == ("A", "B", "C", "D")


def test_max_depth():
    assert max_depth(build_outline("# A\n## B\n### C")) == 3
    assert max_depth(build_outline("# A\n# B")) == 1
    assert max_depth(()) == 0


def test_empty_markdown_yields_empty_outline():
    assert build_outline("") == ()
    assert build_outline("no headings here\njust prose") == ()


def test_node_is_frozen_dataclass():
    (node,) = build_outline("# X")
    assert isinstance(node, OutlineNode)
    with pytest.raises(Exception):
        node.title = "Y"  # type: ignore[misc]


def test_non_heading_hash_without_space_ignored():
    # "#notaheading" (no space) is not an ATX heading.
    assert build_outline("#notaheading") == ()


def test_type_errors():
    with pytest.raises(TypeError):
        build_outline(123)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        flatten_titles("notatuple")  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        max_depth(["x"])  # type: ignore[list-item]


def test_determinism():
    md = "# A\n## B\n## C\n### D"
    assert build_outline(md) == build_outline(md)
