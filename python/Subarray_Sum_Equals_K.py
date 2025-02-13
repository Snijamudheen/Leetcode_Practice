'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.'''

def count_subarrays(arr, k):
    count = 0  # Stores the number of subarrays with sum k
    
    # Loop through each starting index
    for start in range(len(arr)):
        total = 0  # Reset sum for new subarray
        
        # Loop through each ending index
        for end in range(start, len(arr)):
            total += arr[end]  # Add current element to sum
            
            if total == k:  # Check if sum equals k
                count += 1  # Increment count if condition met
    
    return count  # Return the total count

# Example usage
arr = [10, 2, -2, -20, 10]
k = -10
print(count_subarrays(arr, k))  # Output: 3
