"""Problem #12 [Hard]

This problem was asked by Amazon.

There exists a staircase with `N` steps, and you can climb up either 1 or 2
steps at a time. Given `N`, write a function that returns the number of unique
ways you can climb the staircase. The order of the steps matters.

For example, if `N` is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could
climb any number from a set of positive integers `X`? For example, if
`X = {1, 3, 5}`, you could climb 1, 3, or 5 steps at a time.
"""

from typing import Iterable, List


def number_of_ways_1_2_steps(n: int) -> int:
    """Get the number of unique ways you can climb the staircase.

    Solution for the case you can climb up either 1 or 2 steps at a time.
    """

    nways: List[int] = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        nways[i] = nways[i - 1] + nways[i - 2]
    return nways[n]


def number_of_ways_custom(X: Iterable[int], n: int) -> int:
    """Get the number of unique ways you can climb the staircase.

    Solution for the case you can climb up a custom number of steps at a time.
    """

    nways: List[int] = [1] + [0] * n
    for i in range(1, n + 1):
        for x in X:
            if i - x >= 0:
                nways[i] += nways[i - x]

    return nways[n]


if __name__ == '__main__':
    cases_1_2 = [
        (0,    1),
        (1,    1),
        (2,    2),
        (3,    3),
        (4,    5),
        (5,    8),
        (9,   55),
        (11, 144),
    ]

    for n, expected_result in cases_1_2:
        result = number_of_ways_1_2_steps(n)
        assert result == expected_result
        print(f'number_of_ways_1_2_steps({n}) => {result}')

    cases_X = [
        ([1, 2],     0,    1),
        ([1, 2],     1,    1),
        ([1, 2],     2,    2),
        ([1, 2],     3,    3),
        ([1, 2],     4,    5),
        ([1, 2],     5,    8),
        ([1, 2],     9,   55),
        ([1, 2],    11,  144),
        ([2, 5],     1,    0),
        ([2, 5],    10,    2),
        ([1, 2, 3],  0,    1),
        ([1, 2, 3],  1,    1),
        ([1, 2, 3],  4,    7),
        ([1, 2, 3],  5,   13),
        ([1, 2, 5],  5,    9),
        ([1, 3, 5],  5,    5),
    ]

    for X, n, expected_result in cases_X:
        result = number_of_ways_custom(X, n)
        assert result == expected_result
        print(f'number_of_ways_custom({X}, {n}) => {result}')
