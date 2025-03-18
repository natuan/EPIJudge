from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    if not square_matrix:
        return []

    n = len(square_matrix)
    if n == 1:
        return [square_matrix[0][0]]
    border = square_matrix[0] + \
        [square_matrix[i][n-1] for i in range(1, n-1)] + \
        list(reversed(square_matrix[n-1])) + \
        [square_matrix[i][0] for i in range(n-2, 0, -1)]
    
    sub_matrix = [[square_matrix[r][c] for c in range(1, n-1)] for r in range(1, n-1)]

    return border + matrix_in_spiral_order(sub_matrix)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
