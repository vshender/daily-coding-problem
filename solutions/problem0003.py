"""Problem #3 [Medium]

This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes
the tree into a string, and `deserialize(s)`, which deserializes the string
back into the tree.

For example, given the following `Node` class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple


NONE_REPR = '\0'
SEPARATOR = '\n'


@dataclass
class Node:
    val: str
    left: Optional[Node] = None
    right: Optional[Node] = None


def serialize(node: Optional[Node]) -> str:
    """Serialize a binary tree to a string representation."""

    strs: List[str] = []

    def serialize_aux(node: Optional[Node]) -> None:
        if node is not None:
            strs.append(node.val)
            serialize_aux(node.left)
            serialize_aux(node.right)
        else:
            strs.append(NONE_REPR)

    serialize_aux(node)
    return SEPARATOR.join(strs)


def deserialize(node_str: str) -> Optional[Node]:
    """Deserialize a binary tree from a string representation."""

    strs: List[str] = node_str.split(SEPARATOR)

    def deserialize_aux(i: int) -> Tuple[Optional[Node], int]:
        if strs[i] != NONE_REPR:
            val = strs[i]
            left, i = deserialize_aux(i + 1)
            right, i = deserialize_aux(i)
            return Node(val, left, right), i
        else:
            return None, i + 1

    node, _ = deserialize_aux(0)
    return node


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    node_str = serialize(node)
    print(f'serialize   => {node_str!r}')
    node2 = deserialize(node_str)
    print(f'deserialize => {node2}')

    assert node == node2
    assert node2.left is not None
    assert node2.left.left is not None
    assert node2.left.left.val == 'left.left'
