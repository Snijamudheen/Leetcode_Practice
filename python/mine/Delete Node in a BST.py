'''Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if tree is empty, return none
        if not root:
            return None
        
        # if key is smaller than root then go left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # if key is greater than root then go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # found the node to delete
        else:
            if not root.left: # if no left node, then go to right
                return root.right
            
            if not root.right: # if no right node, then go to left
                return root.left

            # we are goignt o find the smallest node in the right subtree
            temp = root.right

            # go to the leftmost value
            while temp.left:
                temp = temp.left

            # replace the root key value with the smallest val we found
            root.val = temp.val

            # delete the duplicate node
            root.right = self.deleteNode(root.right, temp.val)

        return root
