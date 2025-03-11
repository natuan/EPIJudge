from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# Problem 7.2: reverse sublist

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    if not L:
        return None
    if start >= finish:
        return L
    
    before_start = None if start == 1 else L
    for _ in range(start - 2):
        before_start = before_start.next

    sublist_head = before_start.next if before_start else L
    current, next_current = sublist_head, sublist_head.next   
    for _ in range(finish - start):
        # Invariance: sublist of all nodes before and including "current" has been
        # reversed. "next_current" is the next node of "current"
        temp = next_current.next
        next_current.next = current
        current = next_current
        next_current = temp
    # After the for loop above, "current" is at the end of the sublist that has
    # been reversed, and "next_current" is still the next node of "current"
    if before_start:
        before_start.next = current
    else:
        # Head of the original list now changes to "current"
        L = current
    
    # After the operation below, sublist_head is no longer the head of sublist!
    sublist_head.next = next_current
    
    return L

    """
    # My first attempt: not working
    if not L:
        return None
    if start >= finish:
        return L

    # The node at the start - 1 position
    before_start = None if start == 1 else L
    for _ in range(start - 1):
        before_start = before_start.next

    current = before_start.next if before_start else L
    after_current = current.next

    for _ in range(start, finish):
        next_after_current = after_current.next if after_current else None
        if after_current:
            after_current.next = current
            current = after_current
            after_current = next_after_current
    if before_start:
        start_node = before_start.next
        if start_node:
            start_node.next = after_current
        before_start.next = start_node"
    
    return L
    """


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
