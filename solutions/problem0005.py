"""Problem #5 [Medium]

This problem was asked by Jane Street.

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the
first and last element of that pair. For example, `car(cons(3, 4))` returns 3,
and `cdr(cons(3, 4))` returns 4.

Given this implementation of `cons`:

    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair

Implement `car` and `cdr`.
"""

from typing import Any, Callable


PairFunc = Callable[[Any, Any], Any]
Pair = Callable[[PairFunc], Any]


def cons(a: Any, b: Any) -> Pair:
    """Construct a pair."""

    def pair(f: PairFunc) -> Any:
        return f(a, b)
    return pair


def car(pair: Pair) -> Any:
    """Return the first element of a pair."""

    return pair(lambda x, _: x)


def cdr(pair: Pair) -> Any:
    """Return the last element of a pair."""

    return pair(lambda _, x: x)


if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    print('car(cons(3, 4)) =>', car(cons(3, 4)))

    assert cdr(cons(3, 4)) == 4
    print('cdr(cons(3, 4)) =>', cdr(cons(3, 4)))
