'''finds and returns the indices of all occurrences of the character ')' in a given string'''

def find_closing_parentheses(s):
    # Create an empty list to store the indices where ')' is found.
    indices = []
    
    # Loop over the string with both the index (i) and the character (char).
    for i, char in enumerate(s):
        # If the current character is ')', add its index to the list.
        if char == ')':
            indices.append(i)
    
    # Return the list of indices.
    return indices

# Example usage:
if __name__ == "__main__":
    # Example string containing some closing parentheses.
    input_string = "Hello (world))! How (are) you) today?"
    
    # Find all indices of ')'.
    closing_indices = find_closing_parentheses(input_string)
    
    print("Indices of ')':", closing_indices)


# OR

def find_closing_parentheses(s):
    indices = []  # This will store the indices of ')'
    start = 0     # Begin searching from the start of the string
    
    while True:
        # Find the next occurrence of ')' starting from 'start'
        index = s.find(')', start)
        # If no ')' is found, break out of the loop (find() returns -1)
        if index == -1:
            break
        # Append the found index to our list
        indices.append(index)
        # Update 'start' to search for the next occurrence after the current one
        start = index + 1
        
    return indices

# Example usage:
if __name__ == "__main__":
    input_string = "Hello (world))! How (are) you) today?"
    closing_indices = find_closing_parentheses(input_string)
    print("Indices of ')':", closing_indices)
