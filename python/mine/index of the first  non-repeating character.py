# Python program to find the index of the first 
# non-repeating character using a nested loop

# Function to find the first non-repeating character
def nonRepeatingChar(s):
    # Step 2: Iterate over each character in the string
    for i in range(len(s)):
        found = False  # Assume the character is unique

        # Step 3: Compare the current character with all other characters
        for j in range(len(s)):
            # If the character is found at another index (i != j)
            if i != j and s[i] == s[j]:
                found = True  # Character is repeating
                break  # No need to check further, break out of the inner loop

        # Step 4: If the character never repeated, return it
        if not found:
            return s[i]  # First non-repeating character found

    # Step 5: If no unique character is found, return '$' as a placeholder
    return '$'

# Driver code
if __name__ == "__main__":
    s = "racecar"  # Example input string
  
    print(nonRepeatingChar(s))  # Expected output: 'e'
