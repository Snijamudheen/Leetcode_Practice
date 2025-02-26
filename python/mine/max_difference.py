# find the maximum difference where the larger number appears after the smaller number

def max_difference(arr):
    min_value = arr[0]  # Start with the first number
    max_diff = 0  # Start with no difference

    for num in arr[1:]:  # Loop through the list from the second number
        max_diff = max(max_diff, num - min_value)  # Check the difference
        min_value = min(min_value, num)  # Update the smallest number seen

    print(max_diff)

# Read input
n = int(input())  # Read the size of the list
arr = list(map(int, input().split()))  # Read space-separated numbers

# Compute and print result
max_difference(arr)
