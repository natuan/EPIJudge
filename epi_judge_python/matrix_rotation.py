from typing import List

from test_framework import generic_test

# Problem 5.19: rotate matrix 90% clockwise
# See solution for much simpler implementation
from typing import Tuple

def rotate_matrix(square_matrix: List[List[int]]) -> None:
    # TODO - you fill in here.

    def _next_pos(pos: Tuple[int, int], offset: int, matrix_size: int) -> Tuple[int, int]:
        if matrix_size <= 1:
            return pos

        r, c = pos
        if r == offset:
            if c == offset + matrix_size - 1:
                r = offset + 1
            else:
                c += 1
        elif r == offset + matrix_size - 1:
            if c == offset:
                r -= 1
            else:
                c -= 1
        elif c == offset + matrix_size - 1:
            if r == offset + matrix_size - 1:
                c -= 1
            else:
                r += 1
        elif c == offset:
            if r == offset:
                c += 1
            else:
                r -= 1
        return (r, c)

    def _boundary_step(r0, c0, offset, matrix_size):
        # Perform one step clockwise for all elements in the boundary
        # of the matrix with top corner being (r0, c0) and the length
        # being "matrix_size"
        if matrix_size <= 1:
            return
        temp = square_matrix[r0][c0]
        r, c = _next_pos((r0, c0), offset, matrix_size)
        while r != r0 or c != c0:
            square_matrix[r][c], temp = temp, square_matrix[r][c]
            r, c = _next_pos((r, c), offset, matrix_size)
        assert r == r0 and c == c0
        square_matrix[r][c], temp = temp, square_matrix[r][c]

    n = len(square_matrix)
    for offset in range(int(n // 2)):
        matrix_size = n - 2 * offset
        r0 = c0 = offset
        # Rotate submatrix with top left corner being (r0, c0), and
        # the length being "matrix_size"
        for _ in range(matrix_size - 1):
            _boundary_step(r0, c0, offset, matrix_size)

    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
