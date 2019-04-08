"""Problem #9 [Hard]

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, `[2, 4, 6, 2, 5]` should return 13, since we pick 2, 6, and 5.
`[5, 1, 1, 5]` should return 10, since we pick 5 and 5.

Follow-up: Can you do this in `O(N)` time and constant space?
"""

from typing import Sequence, Tuple


def dynamic_programming(numbers: Sequence[int]) -> int:
    """Dynamic programming solution.

    Time: O(n), memory: O(n).
    """

    n = len(numbers)
    if n == 0:
        return 0

    max_sum = [0] * n
    for i in range(0, n):
        without_cur = max_sum[i - 1] if i >= 1 else 0
        with_cur = (max_sum[i - 2] if i >= 2 else 0) + numbers[i]
        max_sum[i] = max(without_cur, with_cur)

    return max_sum[n - 1]


def dynamic_programming_const_mem(numbers: Sequence[int]) -> int:
    """Dynamic programming solution.

    Time: O(n), memory: O(1).
    """

    pprev_sum, prev_sum, largest_sum = 0, 0, 0
    for number in numbers:
        pprev_sum, prev_sum = prev_sum, largest_sum
        largest_sum = max(prev_sum, pprev_sum + number)

    return largest_sum


if __name__ == '__main__':
    cases: Sequence[Tuple[Sequence[int], int]] = [
        ([],                0),
        ([42],             42),
        ([27, 42],         42),
        ([5, 1, 1, 5],     10),
        ([2, 4, 6, 2, 5],  13),
        ([2, 4, 6, 2, -5],  8),
    ]

    for numbers, expected_sum in cases:
        for solve in [dynamic_programming, dynamic_programming_const_mem]:
            largest_sum = solve(numbers)
            print(f'{solve.__name__}({numbers}) => {largest_sum}')
            assert largest_sum == expected_sum
