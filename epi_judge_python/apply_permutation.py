from typing import List

from test_framework import generic_test

# Problem 5.10: apply permutation to array


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    if not A or not perm:
        return
    for i in range(len(A)):
        while perm[i] != i:
            A[i], A[perm[i]] = A[perm[i]], A[i]
            
            # This won't work!!!!: perm[i], perm[perm[i]] = perm[perm[i]], perm[i]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
