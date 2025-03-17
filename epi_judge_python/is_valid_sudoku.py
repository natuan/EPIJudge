from typing import List

from test_framework import generic_test

# Problem 5.17: check valid Sudoku board

import math

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.

    def _is_valid_block(block) -> bool:
        """
        # NOTE: this will fail (notice the we didn't convert filter result to list in defining a)
        a = filter(lambda x: x != 0, block)
        return len(list(a)) == len(set(a))

        The the set(a) above will return empty set!
        """

        a = list(filter(lambda x: x != 0, block))
        return len(list(a)) == len(set(a))
    
    n = len(partial_assignment)

    if any(not _is_valid_block([partial_assignment[i][j] for j in range(n)]) or 
           not _is_valid_block([partial_assignment[j][i] for j in range(n)]) for i in range(n)):
        return False
    
    block_size = int(math.sqrt(n))

    if any(not _is_valid_block([partial_assignment[r][c]
                                for r in range(i * block_size, (i+1)*block_size)
                                for c in range(j * block_size, (j+1)*block_size)])
            for i in range(n//block_size) for j in range(n//block_size)):
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
