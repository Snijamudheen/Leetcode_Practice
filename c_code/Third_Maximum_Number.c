/*Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.*/

class Solution 
{
  public:
    int thirdMax(vector<int>& nums) 
    {
        int maxi1 = INT_MIN;
        int maxi2 = INT_MIN;
        int maxi3 = INT_MIN;
        int flag = 0;

        for(int i = 0; i < nums.size(); i++) 
        {
            if(nums[i] > maxi1) 
            {
                maxi3 = maxi2;
                maxi2 = maxi1;
                maxi1 = nums[i];
            }
            else if(nums[i] < maxi1 && nums[i] > maxi2) 
            {
                maxi3 = maxi2;
                maxi2 = nums[i];
            }
            else if(nums[i] < maxi2 && nums[i] > maxi3) 
                maxi3 = nums[i];

            if(nums[i] == INT_MIN) 
                flag = 1;
        }

        if(nums.size() < 3) 
          return maxi1;
      
        if(nums.size() >= 3 && flag == 0 && maxi3 == INT_MIN) 
          return maxi1;
      
        if(flag == 1 && maxi2 == INT_MIN) 
          return maxi1;
      
        return maxi3;  
    }
};
