"""Problem #2 [Hard]

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index
`i` of the new array is the product of all the numbers in the original array
except the one at `i`.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be
`[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output
would be `[2, 3, 6]`.

Follow-up: what if you can't use division?
"""

from functools import reduce
from operator import mul
from typing import List, Sequence, Tuple


def bruteforce(numbers: Sequence[int]) -> List[int]:
    """Time: O(n^2), memory: O(1)*.

    * I don't count result `products` memory.
    """

    n = len(numbers)
    products = [1] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                products[i] *= numbers[j]
    return products


def using_division(numbers: Sequence[int]) -> List[int]:
    """Time: O(n), memory: O(1)*, using division.

    * I don't count result memory.
    """

    zeros_number = numbers.count(0)
    if zeros_number == 0:
        product = reduce(mul, numbers, 1)
        return [product // number for number in numbers]
    else:
        products = [0] * len(numbers)
        if zeros_number == 1:
            products[numbers.index(0)] = \
                reduce(mul, (num for num in numbers if num != 0), 1)
        return products


def without_division(numbers: Sequence[int]) -> List[int]:
    """Time: O(n), memory: O(n), not using division."""

    n = len(numbers)

    lp = 1
    left_products = []
    for number in numbers:
        lp *= number
        left_products.append(lp)

    rp = 1
    right_products = []
    for number in reversed(numbers):
        rp *= number
        right_products.append(rp)
    right_products.reverse()

    products = [1] * n
    for i in range(n):
        if i - 1 >= 0:
            products[i] *= left_products[i - 1]
        if i + 1 < n:
            products[i] *= right_products[i + 1]

    return products


if __name__ == '__main__':
    cases: List[Tuple[List[int], List[int]]] = [
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([3, 2, 1],       [2, 3, 6]),
        ([],              []),
        ([42],            [1]),
        ([0],             [1]),
        ([0, 0],          [0, 0]),
        ([0, 1, 2, 3],    [6, 0, 0, 0]),
        ([1, 0, 2, 0],    [0, 0, 0, 0]),
    ]

    for numbers, expected_result in cases:
        for solve in [bruteforce, using_division, without_division]:
            result = solve(numbers)
            assert result == expected_result
            print(f'{solve.__name__}({numbers}) => {result}')
