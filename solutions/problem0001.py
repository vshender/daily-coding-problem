"""Problem #1 [Easy]

This problem was recently asked by Google.

Given a list of numbers and a number `k`, return whether any two numbers
from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of 17, return true since 10 + 7 is
17.

Bonus: Can you do this in one pass?
"""

from typing import Dict, Optional, Sequence, Tuple


def bruteforce(numbers: Sequence[int], k: int) -> Optional[Tuple[int, int]]:
    """Time: O(n^2), memory: O(1)."""

    n = len(numbers)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == k:
                return i, j

    return None


def find_sum_pair(numbers: Sequence[int], k: int) -> Optional[Tuple[int, int]]:
    """Time: O(n), memory: O(n)."""

    seen_numbers: Dict[int, int] = {}  # number -> index
    n = len(numbers)

    for i in range(n):
        if k - numbers[i] in seen_numbers:
            return seen_numbers[k - numbers[i]], i
        seen_numbers[numbers[i]] = i

    return None


if __name__ == '__main__':
    cases = [
        ([10, 15, 3, 7], 17, (0, 3)),
        ([1, 2, 5],       4, None),
    ]

    for numbers, k, expected_result in cases:
        for solve in [bruteforce, find_sum_pair]:
            result = solve(numbers, k)
            assert result == expected_result

            print(f'{solve.__name__}({numbers}, {k}) => ', end='')
            if result is not None:
                i, j = result
                print(f'{numbers[i]} + {numbers[j]} = {k}')
            else:
                print('no solution')
