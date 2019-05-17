"""Problem #20 [Easy]

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the
intersecting node. The lists are non-cyclical.

For example, given `A = 3 -> 7 -> 8 -> 10` and `B = 99 -> 1 -> 8 -> 10`, return
the node with value `8`.

In this example, assume nodes with the same value are the exact same node
objects.

Do this in `O(M + N)` time (where `M` and `N` are the lengths of the lists) and
constant space.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    """Linked list node."""

    val: int
    next: Optional[Node] = None

    def __iter__(self):
        yield self.val
        if self.next is not None:
            yield from self.next

    def __len__(self) -> int:
        return 1 + (len(self.next) if self.next is not None else 0)

    def get_nth(self, n: int) -> Optional[Node]:
        """Get `n`th node of the linked list."""

        if n > 0:
            return self.next.get_nth(n - 1) if self.next is not None else None
        else:
            return self


def find_intersection_node(
    a: Optional[Node],
    b: Optional[Node],
) -> Optional[Node]:
    """Find an intersection node of the two given linked lists."""

    la = len(a) if a is not None else 0
    lb = len(b) if b is not None else 0
    if a is not None:
        a = a.get_nth(max(la - lb, 0))
    if b is not None:
        b = b.get_nth(max(lb - la, 0))

    inode = a
    while a is not None:
        assert b is not None
        if a.val != b.val:
            inode = a.next
        a = a.next
        b = b.next

    return inode


def node_to_list(node: Optional[Node]) -> List[int]:
    """Convert the linked list to the Python's list."""

    return list(node) if node is not None else []


if __name__ == '__main__':
    cases = [
        (
            Node(3, Node(7, Node(8, Node(10, None)))),
            Node(99, Node(1, Node(8, Node(10, None)))),
            Node(8, Node(10, None)),
        ),
        (
            Node(6, Node(5, Node(4, Node(3, Node(2, Node(1, None)))))),
            Node(0, Node(4, Node(3, Node(2, Node(1, None))))),
            Node(4, Node(3, Node(2, Node(1, None)))),
        ),
        (
            Node(0, Node(4, Node(3, Node(2, Node(1, None))))),
            Node(6, Node(5, Node(4, Node(3, Node(2, Node(1, None)))))),
            Node(4, Node(3, Node(2, Node(1, None)))),
        ),
        (
            Node(1, Node(2, Node(3, None))),
            Node(1, Node(2, Node(4, None))),
            None,
        ),
        (
            Node(3, Node(7, Node(8, Node(10, None)))),
            None,
            None,
        ),
    ]

    for a, b, expected_inode in cases:
        inode = find_intersection_node(a, b)
        assert inode == expected_inode
        print(
            f'find_intersection_node({node_to_list(a)}, {node_to_list(b)}) '
            f'= {node_to_list(inode)}',
        )
