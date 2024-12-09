from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""
Tuan: this problem, together with 9.3, 9.4, has a pattern: we need to pass necessary information from the ancestors
down to the node when going down the tree.
"""

def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:

    def has_path_sum_helper(node, partial_sum_of_ancestors=0) -> bool:
        if not node:
            return False
        partial_sum_of_ancestors += node.data
        if node.left is None and node.right is None and partial_sum_of_ancestors == remaining_weight:
            return True

        return has_path_sum_helper(node.left, partial_sum_of_ancestors) or has_path_sum_helper(node.right, partial_sum_of_ancestors)        

    return has_path_sum_helper(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
