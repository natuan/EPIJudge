"""
Problem 5.4: check if we could reach end of array from elements' max steps
"""
from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    if not A:
        return False
    furthest_pos = 0
    for i in range(len(A)):
        if furthest_pos < i:
            # We must be able to reach this position i-th
            return False
        furthest_pos = max(furthest_pos, i + A[i])
        if furthest_pos >= len(A) - 1:
            # We're able to reach the end!
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
