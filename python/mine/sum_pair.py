# Find the pairs that add up to a specific sum in a list.

def find_pairs(nums, target):
    # This list will hold all the pairs that add up to the target.
    pairs = []
    
    # Loop over the list using index i.
    for i in range(len(nums)):
        # For each number at index i, look at every number that comes after it.
        for j in range(i + 1, len(nums)):
            # Check if the sum of the two numbers equals the target.
            if nums[i] + nums[j] == target:
                # If they add up to the target, add the pair (as a tuple) to the list.
                pairs.append((nums[i], nums[j]))
    
    # Return the list of pairs.
    return pairs

# Example usage:
if __name__ == "__main__":
    # Define a list of numbers.
    numbers = [1, 2, 3, 4, 5, 6]
    
    # Define the target sum.
    target_sum = 7
    
    # Find and print the pairs that add up to the target sum.
    result = find_pairs(numbers, target_sum)
    print("Pairs that add up to", target_sum, ":", result)
