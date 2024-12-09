from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    
    def sum_root_to_leaf_helper(node, partial_sum = 0) -> int:
        if not node:
            # If one of the left or right is None, we return 0, instead of partial sum.
            # Otherwise, we will over-sum
            return 0
        partial_sum = 2 * partial_sum + node.data
        if not node.left and not node.right:
            return partial_sum
        left_sum = sum_root_to_leaf_helper(node.left, partial_sum=partial_sum)
        right_sum = sum_root_to_leaf_helper(node.right, partial_sum=partial_sum)

        return left_sum + right_sum

    return sum_root_to_leaf_helper(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
