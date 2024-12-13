from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    node_pos_in_inorder = {data: pos for (pos, data) in enumerate(inorder)}
    
    def helper(preorder_start, preorder_end, inorder_start, inorder_end) -> BinaryTreeNode:
        if preorder_start >= preorder_end or inorder_start >= inorder_end:
            return None

        root = BinaryTreeNode(preorder[preorder_start])

        root_pos_in_inorder = node_pos_in_inorder[root.data]
        assert inorder_start <= root_pos_in_inorder < inorder_end

        left_subtree_size = root_pos_in_inorder - inorder_start
        root.left = helper(preorder_start + 1, preorder_start + 1 + left_subtree_size,
                           inorder_start, root_pos_in_inorder)

        right_subtree_size = inorder_end - root_pos_in_inorder + 1
        root.right = helper(preorder_start + 1 + left_subtree_size, preorder_start + 1 + left_subtree_size + right_subtree_size,
                            root_pos_in_inorder + 1, inorder_end)

        return root

    return helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
