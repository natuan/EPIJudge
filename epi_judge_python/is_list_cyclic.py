import functools
from typing import Dict, Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Problem 7.3: Is a list cyclic?
import traceback
import sys

def has_cycle(head: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.

    def _cycle_len(node):
        step = 0
        temp = node
        while True:
            step += 1
            temp = temp.next
            if temp is node:
                break
        return step

    fast = slow = head
    cycle_head = None
    while fast and slow:
        slow = slow.next
        fast = fast.next.next if fast.next else None
        if fast and slow and fast is slow:            
            # Cycle detected!
            advance = head
            for _ in range(_cycle_len(slow)):
                advance = advance.next
            cycle_head = head
            while cycle_head is not advance:
                cycle_head = cycle_head.next
                advance = advance.next
            return cycle_head
    return None



@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
