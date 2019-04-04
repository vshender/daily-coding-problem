"""Return a new sorted merged list from `K` sorted lists, each with size `N`.
"""

import heapq
from typing import List, Sequence, Tuple, TypeVar


T = TypeVar('T')


def merge(lists: Sequence[Sequence[T]]) -> List[T]:
    """Merge sorted lists into a new sorted list."""

    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (
                lists[list_ind][element_ind + 1],
                list_ind,
                element_ind + 1,
            )
            heapq.heappush(heap, next_tuple)

    return merged_list


if __name__ == '__main__':
    cases: List[Tuple[Sequence[Sequence[int]], List[int]]] = [
        ([],                []),
        ([[], [], []],      []),
        ([[], [1], [1, 2]], [1, 1, 2]),
        ([[1]],             [1]),
        (
            [[1], [1, 3, 5], [1, 10, 20, 30, 40]],
            [1, 1, 1, 3, 5, 10, 20, 30, 40],
        ),
    ]

    for lists, expected_result in cases:
        result = merge(lists)
        assert result == expected_result

        print(f'merge({lists}) =>', result)
