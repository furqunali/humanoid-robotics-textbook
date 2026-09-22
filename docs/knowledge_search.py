"""Deterministic lexical search over the textbook knowledge corpus.

The rest of the pipeline builds *toward* retrieval (chunking, citation
indexing, JSONL export) but never actually ranks chunks against a query.
This module closes that gap with a small, dependency-free BM25 index built
directly from :class:`~docs.knowledge_source.KnowledgeChunk` values.

Design goals mirror the surrounding modules:

* **Deterministic** - identical inputs always produce identical, stably
  ordered results (ties broken by ``source``, ``index`` then ``chunk_id``),
  and the index serialises to canonical, ``sort_keys`` JSON.
* **Self-contained** - pure standard library, so it runs in the same test
  environment as the rest of the corpus tooling.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from docs.knowledge_source import KnowledgeChunk

# Standard Robertson/Sparck-Jones BM25 parameters.
BM25_K1 = 1.5
BM25_B = 0.75

_TOKEN = re.compile(r"[^\W_]+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    """Lowercase and split ``text`` into alphanumeric terms.

    Deterministic and Unicode-lowercased so the same document always yields
    the same token stream regardless of source casing or punctuation.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return _TOKEN.findall(text.lower())


@dataclass(frozen=True)
class SearchResult:
    """A single ranked hit against the corpus."""

    chunk_id: str
    source: str
    title: str
    index: int
    score: float

    def to_dict(self) -> dict[str, object]:
        return {
            "chunk_id": self.chunk_id,
            "source": self.source,
            "title": self.title,
            "index": self.index,
            "score": self.score,
        }


@dataclass(frozen=True)
class _Document:
    chunk_id: str
    source: str
    title: str
    index: int
    length: int
    frequencies: dict[str, int]


@dataclass(frozen=True)
class SearchIndex:
    """An immutable BM25 index over a set of knowledge chunks."""

    documents: tuple[_Document, ...]
    document_frequency: dict[str, int]
    average_length: float
    precision: int = field(default=6)

    @property
    def size(self) -> int:
        return len(self.documents)

    def _idf(self, term: str) -> float:
        # BM25 idf with the standard +1 shift so it is always non-negative,
        # even for a term that appears in every document.
        n = self.size
        df = self.document_frequency.get(term, 0)
        if df == 0:
            return 0.0
        return math.log(1 + (n - df + 0.5) / (df + 0.5))

    def _score(self, terms: Counter[str], document: _Document) -> float:
        if not document.length:
            return 0.0
        total = 0.0
        for term, query_count in terms.items():
            tf = document.frequencies.get(term, 0)
            if not tf:
                continue
            idf = self._idf(term)
            if idf <= 0.0:
                continue
            denom = tf + BM25_K1 * (
                1 - BM25_B + BM25_B * document.length / self.average_length
            )
            total += query_count * idf * (tf * (BM25_K1 + 1)) / denom
        return total

    def search(self, query: str, limit: int = 10) -> list[SearchResult]:
        """Return up to ``limit`` chunks ranked by BM25 relevance.

        Only positively-scoring chunks are returned. Results are ordered by
        descending score, with deterministic tie-breaking on
        ``(source, index, chunk_id)`` so the output never depends on the
        original corpus ordering.
        """
        if not isinstance(limit, int) or isinstance(limit, bool) or limit <= 0:
            raise ValueError("limit must be a positive integer")
        terms = Counter(tokenize(query))
        if not terms or not self.documents:
            return []
        scored: list[tuple[float, SearchResult]] = []
        for document in self.documents:
            raw = self._score(terms, document)
            if raw <= 0.0:
                continue
            scored.append(
                (
                    raw,
                    SearchResult(
                    chunk_id=document.chunk_id,
                    source=document.source,
                    title=document.title,
                    index=document.index,
                    score=round(raw, self.precision),
                    ),
                )
            )
        scored.sort(
            key=lambda item: (
                -item[0],
                item[1].source,
                item[1].index,
                item[1].chunk_id,
            )
        )
        return [result for _, result in scored[:limit]]

    def to_dict(self) -> dict[str, object]:
        """Serialise the index into a canonical, JSON-friendly structure."""
        return {
            "average_length": round(self.average_length, self.precision),
            "precision": self.precision,
            "documents": [
                {
                    "chunk_id": document.chunk_id,
                    "source": document.source,
                    "title": document.title,
                    "index": document.index,
                    "length": document.length,
                    "frequencies": dict(sorted(document.frequencies.items())),
                }
                for document in self.documents
            ],
            "document_frequency": dict(sorted(self.document_frequency.items())),
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True)


def build_search_index(
    chunks: Iterable[KnowledgeChunk], *, precision: int = 6
) -> SearchIndex:
    """Build a deterministic BM25 index from knowledge chunks.

    Duplicate chunk ids are rejected (consistent with the citation index and
    retrieval export), keeping every downstream artifact keyed on a unique id.
    """
    if not isinstance(precision, int) or isinstance(precision, bool) or precision < 0:
        raise ValueError("precision must be a non-negative integer")
    documents: list[_Document] = []
    document_frequency: Counter[str] = Counter()
    seen: set[str] = set()
    total_length = 0
    # Validate types before sorting so a bad element raises a clean TypeError
    # rather than an AttributeError from the sort key.
    materialized = list(chunks)
    for chunk in materialized:
        if not isinstance(chunk, KnowledgeChunk):
            raise TypeError("chunks must contain KnowledgeChunk values")
    # Sort up front so the stored document order (and therefore the JSON
    # serialisation) is independent of the caller's ordering.
    for chunk in sorted(materialized, key=lambda item: (item.source, item.index, item.id)):
        if not chunk.id or not chunk.source:
            raise ValueError("chunks require non-empty id and source")
        if chunk.id in seen:
            raise ValueError(f"duplicate chunk id: {chunk.id}")
        seen.add(chunk.id)
        frequencies = Counter(tokenize(chunk.text))
        length = sum(frequencies.values())
        total_length += length
        for term in frequencies:
            document_frequency[term] += 1
        documents.append(
            _Document(
                chunk_id=chunk.id,
                source=chunk.source,
                title=chunk.title,
                index=chunk.index,
                length=length,
                frequencies=dict(frequencies),
            )
        )
    average_length = total_length / len(documents) if documents else 0.0
    return SearchIndex(
        documents=tuple(documents),
        document_frequency=dict(document_frequency),
        average_length=average_length,
        precision=precision,
    )


def write_search_results(results: Iterable[SearchResult], destination: Path) -> int:
    """Write ranked results as deterministic JSON lines; returns the count."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with destination.open("w", encoding="utf-8") as handle:
        for result in results:
            if not isinstance(result, SearchResult):
                raise TypeError("results must contain SearchResult values")
            handle.write(
                json.dumps(result.to_dict(), ensure_ascii=False, sort_keys=True)
            )
            handle.write("\n")
            count += 1
    return count
