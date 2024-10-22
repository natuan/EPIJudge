from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    Result = collections.namedtuple('Result', ('is_balanced', 'height'))    
    
    def is_balanced_binary_tree_helper(node) -> Result:
        if not node:
            return Result(True, 0)
        left_res = is_balanced_binary_tree_helper(node.left)
        if not left_res.is_balanced:
            return Result(False, None)
        right_res = is_balanced_binary_tree_helper(node.right)
        if not right_res.is_balanced:
            return Result(False, None)
        is_balanced = abs(left_res.height - right_res.height) <= 1
        height = max(left_res.height, right_res.height) + 1
        return Result(is_balanced, height)

    return is_balanced_binary_tree_helper(tree).is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
