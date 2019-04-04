"""Problem #4 [Hard]

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input `[3, 4, -1, 1]` should give 2. The input `[1, 2, 0]`
should give 3.

You can modify the input array in-place.
"""

from typing import List, Tuple


def separate_positive_numbers(numbers: List[int]) -> int:
    """Separate positive numbers in a given list.

    This function moves all items less than or equal to zero to the end of the
    list and returns the total number of positive numbers in the list.
    """

    pos = 0

    for i in range(len(numbers)):
        if numbers[i] > 0:
            if i != pos:
                numbers[pos], numbers[i] = numbers[i], numbers[pos]
            pos += 1

    return pos


def find_first_missing_positive(numbers: List[int]) -> int:
    """Find the first missing positive integer in a given list."""

    n = separate_positive_numbers(numbers)

    for i in range(n):
        index = abs(numbers[i]) - 1
        if index < n and numbers[index] > 0:
            numbers[index] *= -1

    for i in range(n):
        if numbers[i] > 0:
            return i + 1

    return n + 1


if __name__ == '__main__':
    cases: List[Tuple[List[int], int]] = [
        ([3, 4, -1, 1],      2),
        ([1, 2, 0],          3),
        ([],                 1),
        ([-1, -2, -3],       1),
        ([-1, -2, -3, 1],    2),
        ([2, 3, 4, 5, 1, 2], 6),
        ([1, 2, 3, 4, 5, 6], 7),
    ]

    for numbers, expected_result in cases:
        print(f'find_first_missing_positive({numbers}) => ', end='')

        result = find_first_missing_positive(numbers)
        assert result == expected_result

        print(result)
