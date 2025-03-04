from test_framework import generic_test
from test_framework.test_failure import TestFailure

# Tuan: to be continued

def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    if x == 0:
        return "0"
    neg = x < 0
    x = -x if x < 0 else x
    s = ""
    while x > 0:
        s += chr(ord('0') + x % 10)
        x /= 10
    if neg:
        s += "-"
    s = reversed(s)
    return s


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    start = 0 if s[0] not in ["-", "+"] else 1
    x = 0
    for i in range(start, len(s)):
        x = x * 10 + int(s[i])
    x = -x if s[0] == '-' else x
    return x


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
