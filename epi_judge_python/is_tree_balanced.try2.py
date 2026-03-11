from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections
import math

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    Result = collections.namedtuple('Result', ('is_balanced', 'height'))

    def helper(node: BinaryTreeNode) -> Result:
        if node is None:
            return Result(True, 0)
        left_res = helper(node.left)
        right_res = helper(node.right)
        if not left_res.is_balanced or not right_res.is_balanced:
            return Result(False, 0)
        is_balanced = abs(left_res.height - right_res.height) <= 1
        height = max(left_res.height, right_res.height) + 1
        return Result(is_balanced, height)
    
    res = helper(tree)
    return res.is_balanced



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
