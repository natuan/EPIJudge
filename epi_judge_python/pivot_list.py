import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Problem 7.12: reorganize list given a pivot


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    if not l:
        return None

    """
    # The following does not work!!! Why?
    #less_dummy_head, equal_dummy_head, greater_dummy_head = [ListNode()] * 3
    #less_it, equal_it, greater_it = less_dummy_head, equal_dummy_head, greater_dummy_head"
    """
    less_it = less_dummy_head = ListNode()
    equal_it = equal_dummy_head = ListNode()
    greater_it = greater_dummy_head = ListNode()
    it = l
    while it:
        if it.data < x:
            less_it.next = it
            less_it = less_it.next
        elif it.data == x:
            equal_it.next = it
            equal_it = equal_it.next
        else:
            greater_it.next = it
            greater_it = greater_it.next
        it = it.next

    greater_it.next = None
    equal_it.next = greater_dummy_head.next
    less_it.next = equal_dummy_head.next
    return less_dummy_head.next



def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
