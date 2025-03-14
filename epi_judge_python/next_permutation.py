from typing import List

from test_framework import generic_test

# Problem 5.11: generate next permutation

def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.
    if not perm:
        return None

    for i in reversed(range(len(perm)-1)):
        if perm[i] < perm[i+1]:
            # perm[i+1:]: decreasing array

            # Find k in [i+1, len) s.t. perm[k] > perm[i] > perm[k+1]
            # We then swap perm[i] and perm[k], then sort perm[i+1:] increasingly
            for k in reversed(range(i+1, len(perm))):
                if perm[k] > perm[i]:
                    perm[k], perm[i] = perm[i], perm[k]
                    break
            perm[i+1:] = reversed(perm[i+1:])
            return perm

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
