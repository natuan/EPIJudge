from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Problem 7.8: remove duplicate nodes from a sorted list

def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    if not L:
        return None
    cur = L
    while cur:
        it = cur
        while it and it.data == cur.data:
            it = it.next
        # Property: "it" is None or "it.data" != "cur.data"
        cur.next = it
        cur = cur.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
