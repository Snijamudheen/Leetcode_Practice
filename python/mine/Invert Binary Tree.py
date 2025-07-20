# Given the root of a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
        # Base case: if the node is empty, do nothing
        if not root:
            return
        
        # Swap the left and right child
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert left subtree
        self.invertTree(root.left)

        # Recursively invert right subtree
        self.invertTree(root.right)

        # Return the root after inverting
        return root
