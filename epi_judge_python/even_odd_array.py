import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    # TODO - you fill in here.
    # Organize elements of array A in the order of even and odd numbers

    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 == 0:
            i += 1
        else:
            # Alway swap when A[i] is odd
            A[i], A[j] = A[j], A[i]
            j -= 1

    """
    # V1: maintain [0, i -1) and [j, -1) as even and odd numbers
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 == 0:
            i += 1
        elif A[j] % 2 != 0:
            j -= 1
        else:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i += 1
            j -= 1
    """
    return


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
