# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers to the start (beg) and end (end) of the array
        beg, end = 0, len(nums) - 1

        # Continue searching as long as the search range is valid
        while beg <= end:
            # Find the middle index of the current range
            mid = (beg + end) // 2

            # If the middle element is the target, return its index. eventually if the target is present then it returns here
            if nums[mid] == target:
                return mid

            # Check if the left half [beg to mid] is sorted
            if nums[beg] <= nums[mid]:
                # If the target is in the range of the sorted left half
                if nums[beg] <= target <= nums[mid]:
                    # Narrow the search to the left half
                    end = mid - 1
                else:
                    # Otherwise, search the right half
                    beg = mid + 1
            else:
                # Otherwise, the right half [mid to end] must be sorted
                if nums[mid] <= target <= nums[end]:
                    # If the target is in the range of the sorted right half
                    beg = mid + 1
                else:
                    # Otherwise, search the left half
                    end = mid - 1

        # If we finish the loop without finding the target, return -1
        return -1 
