import collections
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    
    # A node is ready to processed (i.e., to print out its data) if 
    # its left sub-tree has been processed.
    NodeInfo = collections.namedtuple("NodeInfo", ("node", "is_ready"))
    
    nodes: List[NodeInfo] = [NodeInfo(node=tree, is_ready=False)]
    results = []
    while nodes:
        head = nodes.pop()
        if head.is_ready:
            results.append(head.node.data)
        else:
            if head.node.right:
                nodes.append(NodeInfo(node=head.node.right, is_ready=False))
            
            # Add this head node into the stack again, but this time with is_ready = True
            # because we will add its left sub-tree on top of it. Therefore, when we reach
            # this head node the next time, its left sub-tree will have been processed.
            nodes.append(NodeInfo(node=head.node, is_ready=True))

            if head.node.left:
                nodes.append(NodeInfo(node=head.node.left, is_ready=False))
    return results

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
