"""
Problem 5.2: increment an arbitrary-large integer represented as an array
"""
from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.

    if not A:
        return []
    A.reverse()
    i, carry = 0, 1
    while i < len(A) and carry == 1:
        if A[i] < 9:
            A[i] += 1
            carry = 0
        else:
            A[i] = 0
        i += 1
    if carry == 1:
        A.append(1)
    A.reverse()

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
