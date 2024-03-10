""" Binary Search Trees:
- The height k of a binary search tree is the number of levels in the tree starting from level 0 (root).
- At any level k', # of nodes n = n^(k').
- At the leaf level (k-1), # of nodes, n = 2^(k-1).
- To store a total of N nodes (records) we need a balanced search tree of height at least [log(N) + 1]."""


# TODO: Implement a binary tree using Python.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_from_tuple(binary_tree_tuple):  # Parse the tuple to build a binary tree
    if isinstance(binary_tree_tuple, tuple) and len(binary_tree_tuple) == 3:
        # Hint: If tuple, set node to mid elem, set node.left to first elem and node.right to 3rd elem, then recurse
        node = TreeNode(binary_tree_tuple[1])
        node.left = build_tree_from_tuple(binary_tree_tuple[0])
        node.right = build_tree_from_tuple(binary_tree_tuple[2])
    else:  # if atomic value
        node = TreeNode(binary_tree_tuple)
    return node


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


# Represent the binary tree as a tuple of constant size = 3
tree_tuples = [((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))), ((1, 3, None), 4, 6)]
for tree_tuple in tree_tuples:
    tree = build_tree_from_tuple(tree_tuple)
    print_tree(tree)
