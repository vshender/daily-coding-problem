"""Problem #14 [Medium]

This problem was asked by Google.

The area of a circle is defined as `pi * r^2`. Estimate `pi` to 3 decimal
places using a Monte Carlo method.

Hint: The basic equation of a circle is `x^2 + y^2 = r^2`.
"""

from random import random


def estimate_pi(eps: float) -> float:
    """Estimate `pi` with the given precision using a Monte Carlo method."""

    # When using the Monte Carlo method, we can obtain the required precision
    # only with some probability, so the required number of samples depends on
    # both the required precision and the probability.
    #
    #   See also https://stackoverflow.com/a/33069371/436435
    #
    # Simplifying the calculation error when using a Monte Carlo method is
    # proportional to `sqrt(D / N)`, where `D` is some constant, and `N` is the
    # number of samples.
    #
    # TODO: (WHY?) The constant should be larger in order to obtain acceptable
    # results for `eps = 10e-2`, for which the worst results are observed. For
    # `eps = 1e-1` or `eps = `1e-3`, the constant can be even smaller.
    D = 100

    n = int(D / eps ** 2)
    m = 0
    for _ in range(n):
        x = random()
        y = random()
        if x ** 2 + y ** 2 < 1.:
            m += 1

    return 4 * m / n


def _test(eps: float, ntests: int) -> None:
    """Test the `pi` estimation with the given precision."""

    import math

    print('-' * 79)
    print(f'Test eps={eps} ntests={ntests}')

    err_cnt = 0
    for i in range(ntests):
        pi_e = estimate_pi(eps)
        if abs(int(math.pi / eps) * eps - int(pi_e / eps) * eps) > eps:
            print('*', end=' ')
            err_cnt += 1
        print(pi_e)

    print(f'Number of errors: {err_cnt} / {ntests}\n')


if __name__ == '__main__':
    _test(1e-1, 100)
    _test(1e-2, 100)
    _test(1e-3, 20)
