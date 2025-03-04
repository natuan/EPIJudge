from typing import List

from test_framework import generic_test

import collections

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # TODO - you fill in here.
    if n <= 1:
        return []
    primes = []
    excluded = [False] * (n - 1)  # [2, n]
    for i in range(2, n + 1):
        if not excluded[i - 2]:
            primes.append(i)
            for j in range(2, int(n//i) + 1):
                excluded[i * j - 2] = True
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
