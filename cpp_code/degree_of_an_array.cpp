/*Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.*/

class Solution 
{
    public:
        int findShortestSubArray(vector<int>& nums) 
        {
            
            unordered_map<int,int> first, second, count;
                
            for(int i = 0;i < nums.size(); i++)
            {
                if(first.count(nums[i]) == 0)
                    first[nums[i]] = i;
                
                second[nums[i]] = i;
                count[nums[i]]++;
            }
            
            int maxi = 0;
            
            for(auto i:count)
            {
                maxi = max(maxi, i.second);
            }
            
            cout << maxi;
            int ans = nums.size();
                
            for(auto i:count)
            {
                if(i.second == maxi)
                {
                    ans = min(ans,second[i.first] - first[i.first] + 1);
                }
            }
            
            return ans;
        }
};
