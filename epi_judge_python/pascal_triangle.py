from typing import List

from test_framework import generic_test

# Problem 5.20: Pascal triangle

def generate_pascal_triangle(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    if n <= 0:
        return []
    results = [[1] * (i + 1) for i in range(n)]
    for i in range(1, n):
        for j in range(1, i):
            results[i][j] = results[i-1][j-1] + results[i-1][j]
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
