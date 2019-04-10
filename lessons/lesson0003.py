"""Given the root to a binary tree, return the deepest node."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, NamedTuple, Optional


@dataclass
class Node:
    val: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


class NodeDepth(NamedTuple):
    node: Node
    depth: int


def find_deepest(node: Node) -> NodeDepth:
    """Find the deepest node of a binary tree."""

    if node.left is None and node.right is None:
        return NodeDepth(node, 1)

    if node.left is None:
        assert node.right is not None
        deepest_subnode = find_deepest(node.right)
    elif node.right is None:
        assert node.left is not None
        deepest_subnode = find_deepest(node.left)
    else:
        deepest_subnode = max(
            find_deepest(node.left),
            find_deepest(node.right),
            key=lambda nd: nd.depth,
        )

    return NodeDepth(deepest_subnode.node, deepest_subnode.depth + 1)


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

    node, depth = find_deepest(tree)
    assert node.val == 9
    assert depth == 4

    print('Deepest node:')
    print('  value:', node.val)
    print('  depth:', depth)
