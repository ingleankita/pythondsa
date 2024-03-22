""" Binary Search Trees:
- The height k of a binary search tree is the number of levels in the tree starting from level 0 (root).
- At any level k', # of nodes n = n^(k').
- At the leaf level (k-1), # of nodes, n = 2^(k-1).
- To store a total of N nodes (records) we need a balanced search tree of height at least [log(N) + 1]."""

"""Inorder (L-C-R): Visit the left subtree, then the current node, and finally the right subtree.
Preorder (C-L-R): Visit the current node, then the left subtree, and finally the right subtree.
Postorder (L-R-C): Visit the left subtree, then the right subtree, and finally the current node."""


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


# TODO: Write a function to perform the inorder traversal of a binary tree.
"""Inorder traversal:
1. Traverse left subtree recursively inorder.
2. Traverse the current node.
3. Traverse right subtree recursively inorder."""


def inorder_traversal(node):  # inorder traversal to list
    if node is None:
        return []
    return inorder_traversal(node.left) + [node.value] + inorder_traversal(node.right)


def traverse_in_order_and_print(node):
    if node is None:
        return

    traverse_in_order_and_print(node.left)
    print(node.value, end=' ')
    traverse_in_order_and_print(node.right)


# TODO: Write a function to perform the preorder traversal of a binary tree.
"""Preorder traversal:
1. Traverse the current node.
2. Traverse the left subtree recursively preorder.
3. Traverse the right subtree recursively preorder."""


def preorder_traversal(node):
    if node is None:
        return []
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)


# TODO: Write a function to perform the postorder traversal of a binary tree.
"""Postorder traversal:
1. Traverse the left subtree recursively postorder.
2. Traverse the right subtree recursively postorder.
3. Traverse the current node."""


def postorder_traversal(node):
    if node is None:
        return []
    return postorder_traversal(node.left) + postorder_traversal(node.right) + [node.value]


# Represent the binary tree as a tuple of constant size = 3
tree_tuples = [((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))), ((1, 3, None), 4, 6)]
for tree_tuple in tree_tuples:
    tree = build_tree_from_tuple(tree_tuple)
    print_tree(tree)
    print(inorder_traversal(tree))
    print(preorder_traversal(tree))
    print(postorder_traversal(tree))
