# find the smallest number that is not a twin (i.e., appears only once in the array). If all numbers are twins, we return -1.

# Step 1: Read input values
N = int(input())  # Read the number of elements
arr = list(map(int, input().split()))  # Read the list of numbers

# Step 2: Count occurrences of each number
count_dict = {}  # Dictionary to store frequency of numbers

for num in arr:
    if num in count_dict:
        count_dict[num] += 1  # Increase count if the number already exists
    else:
        count_dict[num] = 1  # First time seeing this number, initialize count to 1

# Step 3: Find non-twin numbers (numbers that appear only once)
non_twin_numbers = []  # List to store non-twin numbers
for num in count_dict:
    if count_dict[num] == 1:  # Check if a number appears once, as in it is not a twin since it has not appeared twice
        non_twin_numbers.append(num)  # Add non_twin to the list

# Step 4: Print the result
if non_twin_numbers:
    print(min(non_twin_numbers))  # Print the smallest non-twin number
else:
    print(-1)  # If all numbers are twins, print -1
