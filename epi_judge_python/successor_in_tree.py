import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not node:
        return None

    if node.right:
        left_most_child = node.right
        while left_most_child.left:
            left_most_child = left_most_child.left
        return left_most_child

    if node.parent:  
        current = node
        parent = current.parent
        while parent and parent.right == current:
            current = parent
            parent = current.parent
        if parent:
            return parent
    return None


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
