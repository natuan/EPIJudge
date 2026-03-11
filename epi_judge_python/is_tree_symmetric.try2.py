from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    
    def is_symmetric_helper(node_1: BinaryTreeNode, node_2: BinaryTreeNode) -> bool:
        if node_1 is None and node_2 is None:
            return True
        if (node_1 is None and node_2 is not None) or (node_1 is not None and node_2 is None):
            return False
        if node_1.data != node_2.data:
            return False
        return is_symmetric_helper(node_1.left, node_2.right) and is_symmetric_helper(node_1.right, node_2.left)

    return tree is None or is_symmetric_helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
