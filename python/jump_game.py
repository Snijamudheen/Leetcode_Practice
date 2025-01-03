# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # goal is at the end of the array, last index

        for i in range(len(nums) - 1, -1, -1): # we are moving from the last index to the first, greedy approach
            if i + nums[i] >= goal: # if the current index plus the jump number which is the array element is greater than the goal index, basically check if the current position can reach the current goal
                goal = i  # then the new goal is the current index/position, then i-- and go thru the loop

        return True if goal == 0 else False # if goal reaches index 0 then that means we reached target so we won the game or else false
