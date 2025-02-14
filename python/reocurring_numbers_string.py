def find_non_repeating_numbers(s):
    # Step 1: Create an empty dictionary to count digits
    count = {}

    # Step 2: Go through each character in the string
    for char in s:
        # Check if it's a number (0-9)
        if char.isdigit():
            # If the number is already in the dictionary, increase its count by 1
            if char in count:
                count[char] += 1
            # If the number is not in the dictionary, add it with a count of 1
            else:
                count[char] = 1

    # At this point, the dictionary contains the count of each digit
    # Example: if input is "1234561256", count = {'1': 2, '2': 2, '3': 1, '4': 1, '5': 2, '6': 2}

    # Step 3: Create an empty list to store numbers that appear only once
    non_repeating = []

    # Step 4: Go through the count dictionary and find digits that appear only once
    for char in count:
        if count[char] == 1:
            non_repeating.append(char)  # Add the number to the list

    # At this point, non_repeating contains only the numbers that appeared exactly once
    # Example: if input is "1234561256", non_repeating = ['3', '4']

    # Step 5: Return the list of non-repeating numbers
    return non_repeating

# Example usage
input_str = "1234561256"  # The string we are checking
result = find_non_repeating_numbers(input_str)  # Call the function

# Print the result
print("Non-repeating numbers:", result)  # Expected output: ['3', '4']
