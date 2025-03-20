from typing import List

from test_framework import generic_test

# Problem 11.1:  search first key in a sorted list
def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    if not A:
        return -1

    lo, hi = 0, len(A) - 1
    found_index = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if A[mid] < k:
            lo = mid + 1
        elif A[mid] == k:
            found_index = mid
            hi = mid - 1
        else:
            # A[mid] > k
            hi = mid - 1

    return found_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
