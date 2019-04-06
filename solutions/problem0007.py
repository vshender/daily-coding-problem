"""Problem #7 [Medium]

This problem was asked by Facebook.

Given the mapping `a = 1`, `b = 2`, ... `z = 26`, and an encoded message,
count the number of ways it can be decoded.

For example, the message `'111'` would give 3, since it could be decoded as
`'aaa'`, `'ka'`, and `'ak'`.

You can assume that the messages are decodable. For example, `'001'` is not
allowed.
"""


def is_valid_two_digit_char(code: str) -> bool:
    """Check if the given two digit encoded message is a valid char."""

    return 10 <= int(code) <= 26


def backtracking(msg: str) -> int:
    """Backtracking solution."""

    if len(msg) <= 1:
        return 1
    elif len(msg) == 2:
        return 1 + (1 if is_valid_two_digit_char(msg) else 0)
    else:
        cnt = backtracking(msg[1:])
        if is_valid_two_digit_char(msg[:2]):
            cnt += backtracking(msg[2:])

        return cnt


def dynamic_programming(msg: str) -> int:
    """Dynamic programming solution.

    Time: O(n), memory: O(n).
    """

    cnts = [1] + [0] * len(msg)

    for i in range(1, len(msg) + 1):
        cnts[i] = cnts[i - 1]
        if i >= 2 and is_valid_two_digit_char(msg[i-2:i]):
            cnts[i] += cnts[i - 2]

    return cnts[len(msg)]


if __name__ == '__main__':
    cases = [
        ('',          1),
        ('1',         1),
        ('11',        2),
        ('91',        1),
        ('19',        2),
        ('111',       3),
        ('1111',      5),
        ('1311',      4),
        ('11231489', 10),
    ]

    for msg, expected_cnt in cases:
        for solve in [backtracking, dynamic_programming]:
            cnt = solve(msg)
            assert cnt == expected_cnt
            print(f'{solve.__name__}({msg!r}) => {cnt}')
        print()
