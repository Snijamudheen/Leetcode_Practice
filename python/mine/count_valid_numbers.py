# count numbers ≤ X whose digits add up to Y

# Step 1: Take input values
X = int(input("Enter the maximum number (X): "))  # Read the max number (e.g., 20)
Y = int(input("Enter the target sum of digits (Y): "))  # Read the target sum (e.g., 5)

# Step 2: Initialize a counter to track valid numbers
count = 0  # This variable stores how many numbers match the condition

# Step 3: Loop through all numbers from 0 to X
for num in range(X + 1):  # We include X, so we loop from 0 to X
    # Step 4: Convert the number to a string so we can access each digit
    num_str = str(num)

    # Step 5: Calculate the sum of the digits of the number
    digit_sum = 0  # Reset sum for each number
    for digit in num_str:  # Loop through each digit in the number
        digit_sum += int(digit)  # Convert digit to integer and add to sum

    # Step 6: Check if the sum of digits is equal to Y
    if digit_sum == Y:
        count += 1  # Increase count if the condition is met

# Step 7: Print the final result
if count > 0:
    print(count)  # Print the number of valid numbers found
else:
    print(-1)  # If no numbers match, print -1
