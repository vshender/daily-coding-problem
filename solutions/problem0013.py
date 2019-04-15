"""Problem #13 [Hard]

This problem was asked by Amazon.

Given an integer `k` and a string `s`, find the length of the longest
substring that contains at most `k` distinct characters.

For example, given `s = "abcba"` and `k = 2`, the longest substring with `k`
distinct characters is `"bcb"`.
"""

from typing import MutableMapping, Tuple


class SeenChars:
    """Distinct chars counter."""

    def __init__(self):
        self.seen_chars: MutableMapping[str, int] = {}
        self.num_of_distinct_chars: int = 0

    def add_char(self, char: str) -> None:
        if char not in self.seen_chars:
            self.seen_chars[char] = 0
            self.num_of_distinct_chars += 1
        self.seen_chars[char] += 1

    def remove_char(self, char: str) -> None:
        self.seen_chars[char] -= 1
        if self.seen_chars[char] == 0:
            del self.seen_chars[char]
            self.num_of_distinct_chars -= 1


def longest_substring(s: str, k: int) -> Tuple[int, int]:
    """Get the length of the longest substring of the given string that
    contains at most `k` distinct characters.

    This function returns a tuple of two numbers:
    - the length of the longest substring;
    - the starting index of the longest substring.

    Time: O(n), memory: O(k).
    """

    seen_chars = SeenChars()
    longest_length, longest_index = 0, 0

    start_index = 0
    for index in range(0, len(s)):
        seen_chars.add_char(s[index])

        while seen_chars.num_of_distinct_chars > k:
            seen_chars.remove_char(s[start_index])
            start_index += 1

        if index - start_index + 1 > longest_length:
            longest_length = index - start_index + 1
            longest_index = start_index

    return longest_length, longest_index


if __name__ == '__main__':
    cases = [
        ("",             3, (0, 0)),
        ("aaa",          0, (0, 0)),
        ("aaabbbbaaa",   1, (4, 3)),
        ("abcba",        2, (3, 1)),
        ("abccbccaaacc", 2, (7, 5)),
        ("abcabcabcabc", 2, (2, 0)),
        ("aaabbcccdddd", 3, (9, 3)),
        ("abcabcabcabc", 3, (12, 0)),
    ]

    for s, k, expected_result in cases:
        l, idx = longest_substring(s, k)
        assert (l, idx) == expected_result

        subs = s[idx:idx + l]
        print(
            f'longest_substring({s!r}, {k}) => {subs!r}'
            f' (idx: {idx}, len: {l})',
        )
