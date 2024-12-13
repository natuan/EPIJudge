import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:

    def reconstruct_preorder_helper(preorder_iter) -> BinaryTreeNode:
        root_data = next(preorder_iter)
        root = BinaryTreeNode(root_data) if root_data else None
        if root:
            root.left = reconstruct_preorder_helper(preorder_iter)  # This moves the iterator as well,
            root.right = reconstruct_preorder_helper(preorder_iter) # so the iterator will be at the beginning of the right sub-tree!
        return root

    return reconstruct_preorder_helper(iter(preorder))


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
