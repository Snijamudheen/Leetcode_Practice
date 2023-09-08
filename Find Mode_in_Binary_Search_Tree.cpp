/*Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.*/

class Solution 
{
    public:
        
        // Do, Inorder traversal and store in a vector, all nodes
        // use map, to count frequency of each node value using the vector
        // find out the max freq from the map
        // iterate over the map, and check which node values are havig frequency == mxfreq
        // store those in the result array and return
        
        vector<int>v;
        
        void in(TreeNode* root) 
        {
            if(!root) 
                return;
            
            in(root->left);
            v.push_back(root->val);
            in(root->right);
        }
        
        vector<int> findMode(TreeNode* root) 
        {
            in(root); // call the inorder
            map<int, int> mp;
            int mxfreq = -1;
            
            vector<int> ans;  // to store and return our answer
            for(int x : v) 
                mp[x]++; // counting frequency of each node values
            
            for(auto it : mp) 
            {
                mxfreq = max(it.second, mxfreq); // looking for max frequency
            }
            
            for(auto it : mp) 
            {
                if(it.second == mxfreq) 
                { // check which is having frequency == mxfreq
                    ans.push_back(it.first);
                }
            }
            return ans;
        }
};
