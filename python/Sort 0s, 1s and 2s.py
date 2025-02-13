'''Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
You need to solve this problem without utilizing the built-in sort function.'''

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        c0, c1, c2 = 0, 0, 0

        # Count the occurrences of 0s, 1s, and 2s
        for num in arr:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        # Place all 0s, then 1s, then 2s
        idx = 0
        
        # Fill the array with 0s
        for i in range(c0):
            arr[idx] = 0
            idx += 1

        # Fill the array with 1s
        for i in range(c1):
            arr[idx] = 1
            idx += 1

        # Fill the array with 2s
        for i in range(c2):
            arr[idx] = 2
            idx += 1

# Test the Solution class
arr = [0, 1, 2, 0, 1, 2]
ob = Solution()  # Create an instance of the Solution class
ob.sort012(arr)  # Call the sort012 method
