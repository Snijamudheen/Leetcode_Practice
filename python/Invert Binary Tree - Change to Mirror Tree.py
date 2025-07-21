'''Given a binary tree, the task is to convert the binary tree to its Mirror tree. Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mirror(root):
    if root is None:
        return

    # Swap the left and right child
    root.left, root.right = root.right, root.left

    # Recursively mirror the left and right subtrees
    mirror(root.left)
    mirror(root.right)
