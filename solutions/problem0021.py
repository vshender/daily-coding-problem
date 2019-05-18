"""Problem #21 [Easy]

This problem was asked by Snapchat.

Given an array of time intervals `(start, end)` for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given `[(30, 75), (0, 50), (60, 150)]`, you should return 2.
"""

from typing import List, Sequence, Tuple


def min_classrooms_required(intervals: Sequence[Tuple[int, int]]) -> int:
    """Calculate the minimum number of classrooms by the time intervals."""

    events: List[Tuple[int, int]] = []
    for interval in intervals:
        events.append((interval[0], 1))
        events.append((interval[1], -1))
    events.sort()

    cur_num, min_num = 0, 0
    for event in events:
        cur_num += event[1]
        if cur_num > min_num:
            min_num = cur_num

    assert cur_num == 0
    return min_num


if __name__ == '__main__':
    cases: Sequence[Tuple[Sequence[Tuple[int, int]], int]] = [
        (
            [(30, 75), (0, 50), (60, 150)],
            2,
        ),
        (
            [
                (150, 240), (59, 120), (0, 60), (90, 180), (30, 90),
                (150, 210), (90, 150),
            ],
            3,
        ),
        (
            [(0, 60)],
            1,
        ),
        (
            [],
            0,
        ),
    ]

    for intervals, expected_min_num in cases:
        min_num = min_classrooms_required(intervals)
        assert min_num == expected_min_num
        print(f'min_classrooms_required({intervals}) = {min_num}')
