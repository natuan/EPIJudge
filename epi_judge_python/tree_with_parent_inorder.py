from enum import Enum
from typing import List, Tuple

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    Status = Enum("Status", [("left_done", 1), ("right_done", 2), ("nothing_done", 3), ("left_and_root_done", 4), ("all_done", 4)])

    def _move_up(current: BinaryTreeNode, status: Status) -> Tuple[BinaryTreeNode, Status]:
        if current.parent and current.parent.left == current:
            status = Status.left_done
        elif current.parent and current.parent.right == current:
            status = Status.all_done
        current = current.parent
        return (current, status)

    if not tree:
        return []
    results = []
    current = tree
    status = Status.nothing_done
    while current:
        if (status == Status.nothing_done and not current.left) or (status == Status.left_done):
            results.append(current.data)
            if current.right:
                status = Status.nothing_done
                current = current.right
            else:
                current, status = _move_up(current, status)
        elif current.left and status == Status.nothing_done:
            current = current.left
        elif status == Status.all_done:
            current, status = _move_up(current, status)

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
