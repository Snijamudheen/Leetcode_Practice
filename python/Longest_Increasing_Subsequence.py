# Given an integer array nums, return the length of the longest strictly increasing subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Step 1: Create a list called LIS where each element starts with 1.
        # This represents the length of the longest increasing subsequence ending at each position.
        LIS = [1] * len(nums)

        # Step 2: Loop through the array from right to left (backward).
        # We do this to check the future elements and build the subsequence backward.
        for i in range(len(nums) - 1, -1, -1):
            # Step 3: For each element at index i, check the elements that come after it (j).
            for j in range(i + 1, len(nums)):
                # Step 4: If nums[i] is less than nums[j], it means we can extend the subsequence.
                if nums[i] < nums[j]:
                    # Update LIS[i] to be the maximum between its current value and 1 + LIS[j].
                    # 1 + LIS[j] means we’re adding nums[i] to the subsequence ending at nums[j].
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # Step 5: Return the longest subsequence found by taking the maximum value in LIS.
        return max(LIS)
