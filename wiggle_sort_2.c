/*Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.*/

void wiggleSort(int* nums, int numsSize)
{
      int arr[5001];
      
      for(int i = 0; i < 5001; i++) 
            arr[i] = 0;
      
      for(int i = 0; i < numsSize; i++)
      {
          arr[nums[i]]++;
      }
      
      int end = 5000;
      int in = 1;   //start to  fill largest value from 1 index
      
       while(in < numsSize && end > -1)
       {
          if(arr[end] == 0)
          { 
                end--; 
                continue;
          }
          else
          {  
                nums[in] = end;
                 in += 2;
                 arr[end]--;
          }
      }
      
      in = 0; // start to fill next set of values from index 0
      
      while(in < numsSize && end > -1)
      {
          if(arr[end] == 0)
          {
                end--; 
                continue;
          }
          else
          {  
                nums[in] = end;
                 in += 2;
                 arr[end]--;
          }
      }
}
