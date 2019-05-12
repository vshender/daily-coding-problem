"""Problem #15 [Medium]

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.
"""

from random import random
from typing import Iterable, Optional, TypeVar


T = TypeVar('T')


def pick_random(items: Iterable[T]) -> Optional[T]:
    """Pick a random element from the stream with uniform probability."""

    # Choose to remember the `i`th element from the stream with probability
    # `1/i`. Then probability of choosing the `i`th element is
    #
    #   P(i) = (1 / i) * (1 - 1 / (i + 1)) * (1 - 1 / (i + 2)) * ...
    #          ... * (1 - 1 / n) =
    #        = (1 / i) * ((i + 1 - 1) / (i + 1)) * ((i + 2 - 1) / (i + 2) * ...
    #          ... * ((n - 1) / n) =
    #        = (1 / i) * (i / (i + 1)) * ((i + 1) / (i + 2)) * ...
    #          ... * ((n - 1) / n) =
    #        = 1 / n

    cur_item: Optional[T] = None

    for i, item in enumerate(items, start=1):
        if random() <= 1 / i:
            cur_item = item

    return cur_item


if __name__ == '__main__':
    NSAMPLES = 3000
    N = 30

    hist = [0] * N
    for _ in range(NSAMPLES):
        rnd = pick_random(range(N))
        assert rnd is not None

        hist[rnd] += 1

    print(f'{NSAMPLES} samples from [0..{N - 1}]:')
    for i in range(N):
        print('{:2d}: {} {}'.format(i, '*' * hist[i], hist[i]))
