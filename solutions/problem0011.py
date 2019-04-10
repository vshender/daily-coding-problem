"""Problem #11 [Medium]

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string `s` and a set
of all possible query strings, return all strings in the set that have `s` as a
prefix.

For example, given the query string `de` and the set of strings
`[dog, deer, deal]`, return `[deer, deal]`.

Hint: Try preprocessing the dictionary into a more efficient data structure to
speed up queries.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Iterator, Mapping, Optional, Sequence


class TrieNode:
    """Prefix tree node."""

    children: Mapping[str, TrieNode]
    val: Optional[str]

    def __init__(self) -> None:
        self.val = None
        self.children = defaultdict(TrieNode)

    def __iter__(self) -> Iterator[str]:
        """Iterate over the prefix tree."""

        if self.val is not None:
            yield self.val

        for subtree in self.children.values():
            yield from subtree

    def insert(self, s: str) -> None:
        """Insert a string to the prefix tree."""

        node = self
        for c in s:
            node = node.children[c]
        node.val = s

    def find(self, s: str) -> Optional[TrieNode]:
        """Find a prefix tree subnode corresponing to the given string."""

        node = self
        for c in s:
            if c not in node.children:
                return None
            node = node.children[c]
        return node


def preprocess_dict(dct: Sequence[str]) -> TrieNode:
    """Preprocess a dictionary into a prefix tree to speed up queries."""

    trie = TrieNode()
    for s in dct:
        trie.insert(s)
    return trie


def get_autocomplete_suggestions(trie: TrieNode, prefix: str) -> Iterator[str]:
    """Get autocomplete suggestions for the given prefix."""

    node = trie.find(prefix)
    if node is None:
        return

    yield from node


if __name__ == '__main__':
    testdata = [
        (
            ['dog', 'deer', 'deal'],
            [
                ('',     ['dog', 'deer', 'deal']),
                ('d',    ['dog', 'deer', 'deal']),
                ('de',   ['deer', 'deal']),
                ('dee',  ['deer']),
                ('deep', []),
            ],
        ),
        (
            ['', 'arrow', 'set', 'strong', 'strongest'],
            [
                ('',           ['', 'arrow', 'set', 'strong', 'strongest']),
                ('a',          ['arrow']),
                ('s',          ['set', 'strong', 'strongest']),
                ('st',         ['strong', 'strongest']),
                ('strong',     ['strong', 'strongest']),
                ('stronge',    ['strongest']),
                ('strongest',  ['strongest']),
                ('strongest.', []),
                ('x',          []),
            ],
        ),
    ]

    for dct, cases in testdata:
        print(f'Dictionary: {dct}')
        trie = preprocess_dict(dct)
        for query, expected_suggestions in cases:
            suggestions = list(get_autocomplete_suggestions(trie, query))
            assert suggestions == expected_suggestions
            print(f'  {query!r:12} => {suggestions}')
