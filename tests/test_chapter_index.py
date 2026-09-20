from docs.chapter_index import ChapterEntry, build_chapter_index, chapter_paths
def test_index_is_sorted_by_order_then_path():
    entries = [ChapterEntry("Two", "02.md", 2), ChapterEntry("One", "01.md", 1), ChapterEntry("Alt", "01-alt.md", 1)]
    assert chapter_paths(entries) == ("01-alt.md", "01.md", "02.md")
def test_empty_index_is_valid():
    assert build_chapter_index([]) == ()
