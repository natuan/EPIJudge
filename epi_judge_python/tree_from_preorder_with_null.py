import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:

    def compute_tree_size(root_index_in_preorder: int) -> int:
        """
        Compute tree size, including null nodes, for the tree at the given root index
        But look at the solution in the book which doesn't need this function, but instead
        moving the iterator along the way.
        """
        if not preorder[root_index_in_preorder]:
            return 1  # null root is counted!
        
        left_tree_start = root_index_in_preorder + 1
        left_tree_size = compute_tree_size(left_tree_start) if left_tree_start < len(preorder) else 0

        right_tree_start = root_index_in_preorder + left_tree_size + 1
        right_tree_size = compute_tree_size(right_tree_start) if right_tree_start < len(preorder) else 0

        return 1 + left_tree_size + right_tree_size

    def reconstruct_preorder_helper(start, end) -> BinaryTreeNode:
        if start >= end:
            return None
        root = BinaryTreeNode(preorder[start]) if preorder[start] else None
        if root:
            left_tree_start = start + 1
            left_tree_size = compute_tree_size(left_tree_start)
            root.left = reconstruct_preorder_helper(left_tree_start, left_tree_start + left_tree_size)

            right_tree_start = left_tree_start + left_tree_size
            right_tree_size = compute_tree_size(right_tree_start)
            root.right = reconstruct_preorder_helper(right_tree_start, right_tree_start + right_tree_size)

        return root

    return reconstruct_preorder_helper(0, len(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
