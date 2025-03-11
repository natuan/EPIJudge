from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Problem 7.7: remove k-th last node in list in one pass

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    if not L:
        return None
    if k < 0:
        return L
    k_ahead_iter = L
    for _ in range(k):
        k_ahead_iter = k_ahead_iter.next
    kth_last_node = L
    prev = ListNode(0, kth_last_node)
    while k_ahead_iter:
        kth_last_node, k_ahead_iter = kth_last_node.next, k_ahead_iter.next
        prev = prev.next
    if prev.next is L:
        return L.next
    else:
        prev.next = kth_last_node.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
