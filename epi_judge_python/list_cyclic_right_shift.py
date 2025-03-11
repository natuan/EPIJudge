from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Problem 7.9: right shift a list

def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    
    def _get_len(head):
        length = 0
        it = head
        while it:
            length += 1
            it = it.next
        return length
    
    if not L:
        return None
      
    len = _get_len(L)
    
    k %= len
    if k <= 0:
        return L

    dummy_head = ListNode(0, L)
    second = dummy_head
    for _ in range(k):
        second = second.next
    first = dummy_head
    while second.next:
        first, second = first.next, second.next
    new_head = first.next
    first.next = None
    second.next = L
    
    return new_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
