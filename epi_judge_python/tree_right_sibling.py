import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    if not tree:
        return

    NodeInfo = collections.namedtuple("NodeInfo", ("node", "level"))
    queue = collections.deque([NodeInfo(node=tree, level=0)])
    prev_node = None
    prev_level = -1
    while queue:
        current, level = queue.popleft()
        if current.left:
            queue.append(NodeInfo(node=current.left, level=level + 1))
        if current.right:
            queue.append(NodeInfo(node=current.right, level=level + 1))
        if prev_node and prev_level == level:
            prev_node.next = current
        prev_node = current
        prev_level = level
    return


def traverse_next(node):
    while node:
        yield node
        node = node.next
    return


def traverse_left(node):
    while node:
        yield node
        node = node.left
    return


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_right_sibling.py',
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
