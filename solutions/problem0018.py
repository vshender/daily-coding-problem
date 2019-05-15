"""Problem #18 [Hard]

This problem was asked by Google.

Given an array of integers and a number `k`, where `1 <= k <= length` of the
array, compute the maximum values of each subarray of length `k`.

For example, given `array = [10, 5, 2, 7, 8, 7]` and `k = 3`, we should get:
`[10, 7, 8, 8]`, since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

Do this in `O(n)` time and `O(k)` space. You can modify the input array
in-place and you do not need to store the results. You can simply print them
out as you compute them.
"""

from collections import deque
from typing import Deque, Iterable, Sequence


def get_sliding_window_max(numbers: Sequence[int], k: int) -> Iterable[int]:
    """Get the maximum values of each subarray of length `k` of a given array.
    """

    assert 1 <= k <= len(numbers)

    # Deque to store useful for calculation number indices.
    dq: Deque[int] = deque()

    for i in range(k):
        while dq and numbers[dq[-1]] < numbers[i]:
            dq.pop()

        dq.append(i)

    yield numbers[dq[0]]

    for i in range(k, len(numbers)):
        while dq[0] <= i - k:
            dq.popleft()

        while dq and numbers[dq[-1]] < numbers[i]:
            dq.pop()

        dq.append(i)

        yield numbers[dq[0]]


if __name__ == '__main__':
    cases = [
        (
            [10, 5, 2, 7, 8, 7],
            3,
            [10, 7, 8, 8],
        ),
        (
            [1, 2, 3, 4, 3, 2, 5, 6, 4],
            3,
            [3, 4, 4, 4, 5, 6, 6],
        ),
        (
            [10, 5, 2, 12, 7, 9, 9, 10, 4, 15, 14, 13],
            4,
            [12, 12, 12, 12, 10, 10, 15, 15, 15],
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            4,
            [4, 5, 6, 7, 8, 9, 10],
        ),
        (
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            4,
            [10, 9, 8, 7, 6, 5, 4],
        ),
        (
            [10, 5, 2, 7],
            4,
            [10],
        ),
        (
            [42],
            1,
            [42],
        ),
    ]

    for (numbers, k, expected_result) in cases:
        result = list(get_sliding_window_max(numbers, k))
        assert result == expected_result
        print(f'sliding_max({numbers}, {k}) = {result}')
