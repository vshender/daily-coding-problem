"""Problem #19 [Medium]

This problem was asked by Facebook.

A builder is looking to build a row of `N` houses that can be of `K` different
colors. He has a goal of minimizing cost while ensuring that no two neighboring
houses are of the same color.

Given an `N` by `K` matrix where the `n`th row and `k`th column represents the
cost to build the `n`th house with `k`th color, return the minimum cost which
achieves this goal.
"""

import sys
from typing import Sequence


def get_minimum_building_cost(costs: Sequence[Sequence[float]]) -> float:
    """Get the minimum houses building cost given a costs matrix.

    Time: O(n * k^2), memory: O(k).
    """

    num_houses = len(costs)
    num_colors = len(costs[0])

    cur_costs, prev_costs = [0.] * num_colors, [0.] * num_colors

    for house_idx in range(num_houses):
        prev_costs, cur_costs = cur_costs, prev_costs

        for color_idx in range(num_colors):
            cur_costs[color_idx] = sys.maxsize
            for prev_color_idx in range(num_colors):
                if house_idx == 0 or prev_color_idx != color_idx:
                    cur_cost = prev_costs[prev_color_idx] \
                        + costs[house_idx][color_idx]
                    if cur_cost < cur_costs[color_idx]:
                        cur_costs[color_idx] = cur_cost

    return min(cur_costs)


def get_minimum_building_cost_opt(costs: Sequence[Sequence[float]]) -> float:
    """Get the minimum houses building cost given a costs matrix.

    Optimized version. Time: O(n * k), memory: O(k).
    """

    num_houses = len(costs)
    num_colors = len(costs[0])

    min_cost, min_cost_last_color_idx = 0., -1
    second_min_cost = 0.

    cur_costs = [0.] * num_colors

    for house_idx in range(num_houses):
        for color_idx in range(num_colors):
            if color_idx != min_cost_last_color_idx:
                cur_costs[color_idx] = min_cost + costs[house_idx][color_idx]
            else:
                cur_costs[color_idx] = second_min_cost + \
                    costs[house_idx][color_idx]

        min_cost, min_cost_last_color_idx = cur_costs[0], 0
        second_min_cost = sys.maxsize
        for color_idx in range(1, num_colors):
            if cur_costs[color_idx] < min_cost:
                second_min_cost = min_cost
                min_cost = cur_costs[color_idx]
                min_cost_last_color_idx = color_idx
            elif cur_costs[color_idx] < second_min_cost:
                second_min_cost = cur_costs[color_idx]

    return min(cur_costs)


if __name__ == '__main__':
    cases = [
        (
            [
                [42],
            ],
            42,
        ),
        (
            [
                [1, 2, 3, 4],
                [1, 2, 3, 4],
                [1, 2, 3, 4],
            ],
            4,
        ),
        (
            [
                [1, 2, 3, 4],
                [2, 2, 3, 4],
                [5, 3, 5, 5],
            ],
            7,
        ),
        (
            [
                [1, 2, 3],
                [1, 4, 5],
                [2, 3, 1],
                [2, 1, 3],
                [4, 2, 5],
            ],
            8,
        ),
    ]

    for costs, expected_result in cases:
        print(f'costs: {costs}')
        for solver in [
            get_minimum_building_cost,
            get_minimum_building_cost_opt,
        ]:
            result = solver(costs)
            assert result == expected_result

            print(f'{solver.__name__}(costs) = {result}')

        print()
