# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        s1 = []
        s2 = []

        if root is None:
            return res

        s1.append(root)

        while s1 or s2:
            level = []
            while s1:
                curr = s1.pop()
                level.append(curr.val)

                if curr.left:
                    s2.append(curr.left)
                if curr.right:
                    s2.append(curr.right)
            if level:
                res.append(level)

            level = []
            while s2:
                curr = s2.pop()
                level.append(curr.val)

                if curr.right:
                    s1.append(curr.right)
                if curr.left:
                    s1.append(curr.left)

            if level:
                res.append(level)

        return res
