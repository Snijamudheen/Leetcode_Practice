/*You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to 
another number in the set, which results in repetition of one number and loss of another number. You are given an integer array nums representing the data status 
of this set after the error. Find the number that occurs twice and the number that is missing and return them in the form of an array.*/

class Solution 
{
    public:
        vector<int> findErrorNums(vector<int>& nums) 
        {  
            int a;
            int b;
            vector<int> ans;
            int n = nums.size();
            vector arr(n, 0);
            
            for(int i = 0; i < nums.size(); i++)
                arr[nums[i] - 1]++;
            
            for(int i = 0; i < n; i++)
            {
                if(arr[i] == 2)
                    a = i + 1;
                else if(arr[i] == 0)
                    b = i + 1;
            }
            
            ans.push_back(a);
            ans.push_back(b);
            
            return ans;
        }
}; 
