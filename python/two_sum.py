'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is a "map" (or dictionary) to remember numbers we've seen
        # It will store {number: index} pairs
        prevMap = {}

        # Go through each number in the list
        for i, n in enumerate(nums):
            # Figure out what number we need to add to 'n' to get the target
            diff = target - n

            # Check if we've already seen that needed number before
            if diff in prevMap:
                # If we have, return the two indices (where we saw it and the current index)
                return [prevMap[diff], i]

            # If we haven't seen the needed number, remember this one for later
            prevMap[n] = i

        # If no pair is found (shouldn't happen based on problem description), return nothing
        return
