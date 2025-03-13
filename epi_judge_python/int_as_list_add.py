from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Problem 7.13: add list-based integers
# See solution for much simpler implementation

def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    if not L1:
        return L2
    if not L2:
        return L1
    
    it = result_dummy_head = ListNode()
    l1_it, l2_it = L1, L2
    carry = 0
    while l1_it and l2_it:
        it.next = ListNode((l1_it.data + l2_it.data + carry) % 10)
        carry = (l1_it.data + l2_it.data + carry) // 10
        it, l1_it, l2_it = it.next, l1_it.next, l2_it.next
    remain_it = l1_it if not l2_it else l2_it
    while remain_it:
        it.next = ListNode((remain_it.data + carry) % 10)
        carry = (remain_it.data + carry) // 10
        it, remain_it = it.next, remain_it.next
    if carry:
        it.next = ListNode(1)

    return result_dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
