/*Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.*/

class Solution {
public:
    int tiltSum = 0;
    int findTilt(TreeNode* root) {
        DFS(root);
        return tiltSum;
    }
    int DFS(TreeNode* root) {
        if(!root) return 0;
        int leftSum = DFS(root -> left);                // sum of left subtree
        int rightSum = DFS(root -> right);              // sum of right subtree
        tiltSum += abs(leftSum - rightSum);             // add tilt of current node to overall tiltSum
        return leftSum + rightSum + root -> val;        // returns sum of subtree starting at 'root'
    }
};
