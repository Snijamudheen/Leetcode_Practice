# Given an integer array nums, find a subarray that has the largest product, and return the product. The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize prefix and suffix products to 1
        prefix, suffix = 1, 1
        
        # Initialize ans to the first element of the list
        # This handles the case where the list has only one element or all elements are negative
        ans = nums[0]
        
        # Get the length of the list
        n = len(nums)

        # Iterate through the array to calculate the prefix and suffix products
        for i in range(n):
            # If the prefix product becomes 0 (due to encountering a zero in the array),
            # reset it to 1 to start a new subarray product
            if prefix == 0:
                prefix = 1
            
            # Similarly, reset the suffix product to 1 if it becomes 0
            if suffix == 0:
                suffix = 1

            # Multiply the current element to the prefix product
            prefix *= nums[i]
            
            # Multiply the corresponding element from the end to the suffix product
            suffix *= nums[n - i - 1]
            
            # Update the maximum product so far by comparing with prefix and suffix
            ans = max(ans, prefix, suffix)

        # Return the maximum product of any subarray
        return ans
