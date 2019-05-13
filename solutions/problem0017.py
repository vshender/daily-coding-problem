"""Problem #17 [Hard]

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:

    dir
        subdir1
        subdir2
            file.ext

The directory `dir` contains an empty sub-directory `subdir1` and a
sub-directory `subdir2` containing a file `file.ext`.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`
represents:

    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext

The directory `dir` contains two sub-directories `subdir1` and `subdir2`.
`subdir1` contains a file `file1.ext` and an empty second-level sub-directory
`subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2`
containing a file `file2.ext`.

We are interested in finding the longest (number of characters) absolute path
to a file within our file system. For example, in the second example above,
the longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its
length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:
- The name of a file contains at least a period and an extension.
- The name of a directory or sub-directory will not contain a period.
"""

from itertools import takewhile
from typing import List, Optional


def isfilename(name: str) -> bool:
    """Check if the given name is a file name."""

    return '.' in name


def find_longest_abspath(fs_str: str) -> Optional[str]:
    """Find the longest absolute path to a file within the given file system.
    """

    longest_path: Optional[str] = None
    state: List[str] = []

    for fs_item_str in fs_str.split('\n'):
        depth = sum(1 for _ in takewhile(lambda c: c == '\t', fs_item_str))
        fs_item = fs_item_str[depth:]

        if len(state) < depth or depth > 0 and isfilename(state[depth - 1]):
            raise ValueError('invalid FS string representation')

        state[depth:] = [fs_item]

        if isfilename(fs_item):
            path = '/'.join(state)
            if longest_path is None or len(longest_path) < len(path):
                longest_path = path

    return longest_path


if __name__ == '__main__':
    cases = [
        (
            'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext',
            'dir/subdir2/file.ext',
        ),
        (
            'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1'
            '\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
            'dir/subdir2/subsubdir2/file2.ext',
        ),
        (
            'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n'
            '\t\t\tfile2.ext\n\t\t\tsubsubsubdir1\n'
            '\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile3.ext',
            'dir/subdir1/subsubdir1/file2.ext',
        ),
        (
            'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n'
            '\t\t\tfile2.ext\n\t\t\tsubsubsubdir1\n'
            '\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile3.ext\n'
            '\t\t\tsubsubsubdir2\n\t\t\t\tfile4.ext',
            'dir/subdir2/subsubdir2/subsubsubdir2/file4.ext',
        ),
        (
            'dir\n\tsubdir1\n\tsubdir2\n\t\tsubsubdir1',
            None,
        ),
    ]

    for fs_str, expected_longest_path in cases:
        print(fs_str)

        longest_path = find_longest_abspath(fs_str)
        assert longest_path == expected_longest_path
        longest_path_len = len(longest_path) if longest_path is not None else 0

        print(
            f'Longest absolute path: {longest_path!r} '
            f'(lenght: {longest_path_len})\n',
        )
