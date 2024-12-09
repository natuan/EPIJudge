from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_symmetric(tree: BinaryTreeNode) -> bool:
    
    def is_symmetric_helper(left_tree, right_tree):
        if left_tree is None and right_tree is None:
            return True
        if left_tree is not None and right_tree is not None:
            return left_tree.data == right_tree.data and \
                is_symmetric_helper(left_tree.left, right_tree.right) and \
                is_symmetric_helper(left_tree.right, right_tree.left)
        else:
            return False

    if tree is None:
        return True
    return is_symmetric_helper(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
