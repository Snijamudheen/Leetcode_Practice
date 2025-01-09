# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, 1
        two_sum = 0
        res = 0

        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                two_sum = nums[l] + nums[r]
                if two_sum == target:
                    return [l,r]
