"""Build a nested outline tree from Markdown ATX headings.

Given Markdown source, :func:`build_outline` returns a forest of
:class:`OutlineNode` values that mirror the document's heading hierarchy. Only
ATX headings (``#`` .. ``######``) are recognized; fenced code blocks are
ignored so ``#`` comments in code do not pollute the outline.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)(?:\s+#+)?\s*$")
_FENCE_RE = re.compile(r"^\s*(```|~~~)")


@dataclass(frozen=True)
class OutlineNode:
    """A heading and its nested child headings.

    Attributes:
        level: ATX heading level, 1 (``#``) through 6 (``######``).
        title: The heading text with surrounding whitespace stripped.
        children: Child headings nested directly beneath this one.
    """

    level: int
    title: str
    children: tuple["OutlineNode", ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class _Heading:
    level: int
    title: str


def parse_headings(markdown: str) -> tuple[_Heading, ...]:
    """Return the flat sequence of ATX headings in ``markdown``.

    Raises:
        TypeError: If ``markdown`` is not a string.
    """
    if not isinstance(markdown, str):
        raise TypeError("markdown must be a string")
    headings: list[_Heading] = []
    in_fence = False
    for line in markdown.splitlines():
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = _HEADING_RE.match(line)
        if match:
            title = match.group(2).strip()
            headings.append(_Heading(level=len(match.group(1)), title=title))
    return tuple(headings)


def _build(headings: list[_Heading], index: int, level: int) -> tuple[list[OutlineNode], int]:
    nodes: list[OutlineNode] = []
    while index < len(headings):
        heading = headings[index]
        if heading.level <= level:
            break
        children, index = _build(headings, index + 1, heading.level)
        nodes.append(
            OutlineNode(level=heading.level, title=heading.title, children=tuple(children))
        )
    return nodes, index


def build_outline(markdown: str) -> tuple[OutlineNode, ...]:
    """Build a nested outline forest from Markdown ATX headings.

    Deeper headings become children of the nearest shallower heading above
    them. Headings that skip levels (e.g. an ``###`` directly under a ``#``)
    are attached to the nearest valid ancestor without inventing placeholders.

    Args:
        markdown: The Markdown source.

    Returns:
        A tuple of top-level :class:`OutlineNode` values.

    Raises:
        TypeError: If ``markdown`` is not a string.
    """
    headings = list(parse_headings(markdown))
    nodes, _ = _build(headings, 0, 0)
    return tuple(nodes)


def flatten_titles(nodes: tuple[OutlineNode, ...]) -> tuple[str, ...]:
    """Return every node title in depth-first (document) order.

    Raises:
        TypeError: If ``nodes`` is not a tuple/list of :class:`OutlineNode`.
    """
    if not isinstance(nodes, (tuple, list)):
        raise TypeError("nodes must be a tuple or list of OutlineNode values")
    titles: list[str] = []
    for node in nodes:
        if not isinstance(node, OutlineNode):
            raise TypeError("nodes must contain OutlineNode values")
        titles.append(node.title)
        titles.extend(flatten_titles(node.children))
    return tuple(titles)


def max_depth(nodes: tuple[OutlineNode, ...]) -> int:
    """Return the deepest nesting level of the outline (0 when empty)."""
    if not isinstance(nodes, (tuple, list)):
        raise TypeError("nodes must be a tuple or list of OutlineNode values")
    depth = 0
    for node in nodes:
        if not isinstance(node, OutlineNode):
            raise TypeError("nodes must contain OutlineNode values")
        depth = max(depth, 1 + max_depth(node.children))
    return depth
