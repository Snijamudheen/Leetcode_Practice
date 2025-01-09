'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        l, r = 0 , 0
        min_len = float('inf')
        n = len(nums)

        for r in range(n):
            cur_sum += nums[r] # adding right values to the total since we looping thru right values and incrementing that
            while cur_sum >= target and l <= r:
                min_len = min(min_len, r-l+1) # update min length
                cur_sum -= nums[l] # shrink window from left, meaning we leaving out the left most value so subtract that from sum
                l += 1 # move the pointer
        return 0 if min_len == float('inf') else min_len
