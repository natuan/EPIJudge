from test_framework import generic_test

import math

# Problem 4.9: is a decimal integer panlindromic?

def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x < 0:
        return False    
    n = math.floor(math.log10(x)) + 1 if x > 0 else 1
    while n > 1:
        msd, x = divmod(x, 10 ** (n - 1))
        x, lsd = divmod(x, 10)
        if msd != lsd:
            return False
        n -= 2

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
