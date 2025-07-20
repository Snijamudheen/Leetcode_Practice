'''Given a string, remove all spaces from the string and return it. '''

def removeSpaces(s):
    result = []  # List to hold characters that are not spaces

    for char in s:
        if char != ' ':          # If the character is not a space
            result.append(char)  # Add it to the result list

    return ''.join(result)       # Convert list back to a string

# Example usage
text = "g  eeks  for ge  eeks  "
print(removeSpaces(text))  # Output: "geeksforgeeeks"
