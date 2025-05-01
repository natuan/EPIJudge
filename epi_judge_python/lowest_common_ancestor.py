import collections
import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import collections

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    
    Result = collections.namedtuple("Result", ("found_node0", "found_node1", "lca"))
    
    def lca_helper(root, n0, n1) -> Result:
        if not root:
            return Result(False, False, None)
        
        lca_left = lca_helper(root.left, n0, n1)
        if lca_left.lca:
            return lca_left
        
        lca_right = lca_helper(root.right, n0, n1)
        if lca_right.lca:
            return lca_right
        
        found_node0 = lca_left.found_node0 or lca_right.found_node0 or root == n0
        found_node1 = lca_left.found_node1 or lca_right.found_node1 or root == n1
        lca = root if found_node0 and found_node1 else None
        return Result(found_node0, found_node1, lca)
        
    res = lca_helper(tree, node0, node1)
    return res.lca


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
