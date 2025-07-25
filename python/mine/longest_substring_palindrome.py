# find the longest palindrome substring from a given string

def find_longest_palindrome(inputStr):
    n = len(inputStr)  # Get the length of the string
    longest_palindrome = ""  # Store the longest palindrome found

    # Step 1: Generate all possible substrings
    for i in range(n):  # Start position of substring
        for j in range(i + 1, n + 1):  # End position (must be at least i+1 to get substrings of length > 1)
            sub_str = inputStr[i:j]  # Extract substring from index i to j-1

''' Example: inputStr = "ABC"
n = 3

Loop execution:

i = 0
j = 1 → inputStr[0:1] → "A"

j = 2 → inputStr[0:2] → "AB"

j = 3 → inputStr[0:3] → "ABC"

i = 1
j = 2 → inputStr[1:2] → "B"

j = 3 → inputStr[1:3] → "BC"

i = 2
j = 3 → inputStr[2:3] → "C"

Collected Substrings in Order:
"A"

"AB"

"ABC"

"B"

"BC"

"C"'''
            # Step 2: Check if the substring is a palindrome (same forward and backward)
            if sub_str == sub_str[::-1]:  
                
                # Step 3: Update longest palindrome if it's bigger
                if len(sub_str) > len(longest_palindrome):
                    longest_palindrome = sub_str  # Found a longer palindrome!

                # Step 4: If same length as current longest, pick the lexicographically smaller one meaning alphabetically it comes early.
                elif len(sub_str) == len(longest_palindrome) and sub_str < longest_palindrome:
                    longest_palindrome = sub_str  # Pick the smaller one alphabetically

    # Step 5: If no palindrome found, return "None"
    return longest_palindrome if longest_palindrome else "None"

# Step 6: Read user input (a string of uppercase letters)
inputStr = input().strip()

# Step 7: Find the longest palindrome and print the result
print(find_longest_palindrome(inputStr))
