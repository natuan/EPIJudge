from list_node import ListNode
from test_framework import generic_test

# Problem 7.11: is list palindromic?

import math
def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.

    def _get_len(head):
        length = 0
        it = head
        while it:
            length += 1
            it = it.next
        return length
    
    def _reverse_list(head):
        if not head:
            return None
        cur, next_cur = head, head.next
        while next_cur:
            # Invariance: everything before and including "cur" is reversed
            temp = next_cur.next
            next_cur.next = cur
            cur = next_cur
            next_cur = temp
        return cur


    len = _get_len(L)
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(math.floor(len/2)):
        sublist_head = sublist_head.next
    
    sublist_tail = _reverse_list(sublist_head)
    head, tail = L, sublist_tail
    for _ in range(math.floor(len/2)):
        if head.data != tail.data:
            return False
        head, tail = head.next, tail.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
