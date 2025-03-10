from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Problem 7.1: merge sorted lists

def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.

    # 2nd try to review
    if not L1:
        return L2
    if not L2:
        return L1
    data = L1.data if L1.data < L2.data else L2.data
    head = ListNode(data, None)
    tail = head
    if L1.data < L2.data:
        L1 = L1.next
    else:
        L2 = L2.next
    while L1 and L2:
        data = L1.data if L1.data < L2.data else L2.data
        tail.next = ListNode(data)
        tail = tail.next
        if L1.data < L2.data:
            L1 = L1.next
        else:
            L2 = L2.next
    remaining = L1 if L1 else L2
    tail.next = remaining
    return head
    
    """
    # See the book for a simpler implementation!
    if not L1:
        return L2
    if not L2:
        return L1
    l1, l2 = L1, L2
    head = ListNode(l1.data) if l1.data < l2.data else ListNode(l2.data)
    tail = head
    if l1.data < l2.data:
        l1 = l1.next
    else:
        l2 = l2.next

    while l1 and l2:
        tail.next = ListNode(l1.data) if l1.data < l2.data else ListNode(l2.data)
        if l1.data < l2.data:
            l1 = l1.next
        else:
            l2 = l2.next
        tail = tail.next

    remaining = l1 if l1 else l2
    while remaining:
        tail.next = ListNode(remaining.data)
        tail = tail.next
        remaining = remaining.next

    return head
    """


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
