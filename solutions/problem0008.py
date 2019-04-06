"""Problem #8 [Easy]

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def count_unival_subtrees(tree: Optional[Node]) -> int:
    """Count the number of unival subtrees of a tree."""

    if tree is None:
        return 0

    is_unival_tree = 1
    if tree.left is not None:
        is_unival_tree &= tree.val == tree.left.val
    if tree.right is not None:
        is_unival_tree &= tree.val == tree.right.val

    return (
        is_unival_tree +
        count_unival_subtrees(tree.left) + count_unival_subtrees(tree.right)
    )


if __name__ == '__main__':
    cases = (
        (None,                                                          0),
        (Node(1),                                                       1),
        (Node(0, Node(1), Node(1)),                                     2),
        (Node(0, Node(0), Node(1)),                                     2),
        (Node(1, Node(1), Node(1)),                                     3),
        (Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))), 5),
    )

    for tree, expected_count in cases:
        count = count_unival_subtrees(tree)
        assert count == expected_count
        print(f'count_unival_subtrees({tree}) => {count}')
