from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Problem 7.10: even-odd list merge

def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    if not L:
        return None
    even_it, odd_it = L, L.next
    even_list_tail, odd_list_head = even_it, odd_it
    while even_it and odd_it:
        even_list_tail = even_it
        even_it.next = odd_it.next
        if even_it.next:
            odd_it.next = even_it.next.next
        even_it, odd_it = even_it.next, odd_it.next
    even_list_tail = even_it if even_it else even_list_tail
    even_list_tail.next = odd_list_head
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
