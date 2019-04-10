"""Given the root to a binary tree, count the total number of nodes there are.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    val: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


def count(tree: Optional[Node]) -> int:
    """Count the total number of nodes in a binary tree."""

    return 1 + count(tree.left) + count(tree.right) if tree is not None else 0


if __name__ == '__main__':
    tree = Node(
        3,
        Node(2, Node(1)),
        Node(5, Node(4), Node(7, None, Node(9))),
    )
    """
          3
         / \
        2   5
       /   / \
      1   4   7
               \
                9
    """

    nn = count(tree)
    assert nn == 7
    print(f'count(tree) == {nn}')
