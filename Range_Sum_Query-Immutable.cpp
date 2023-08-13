/*Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right 
inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).*/

class NumArray 
{ 
  public:
      vector<int>& preSum; 
      
      NumArray(vector<int>& nums) : preSum(nums) 
      {
          for (int i = 1; i < preSum.size(); ++i)
              preSum[i] += preSum[i-1]; 
      }
      
      int sumRange(int left, int right) 
      {
          if (left == 0) 
              return preSum[right];
          return preSum[right] - preSum[left-1];
      }
};
