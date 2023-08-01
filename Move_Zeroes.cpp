/*Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.*/

class Solution 
{
  public:
    void moveZeroes(vector<int>& nums) 
    {
        int n = nums.size();
        int start = 0, end = n - 1, mid = 0;
      
        while(mid <= end)
        {
            if(nums[mid] != 0)
            {
                swap(nums[start], nums[mid]);                  
                start++;
            }
            mid++;
        }
    }
};
