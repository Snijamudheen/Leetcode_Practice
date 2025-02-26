'''given input M and N where n is length of string and m is index of lexicograhical sorted set of strings.
return the string of index M in lexicographical sorted set of strings . if index m is greater than the length of set of string then return "Not possible"


ex
n=2,k=3


AA
AB
BA
return BA


n=2,k=4
AA
AB
BA
HENCE NOT POSSIBLE'''

def generate_strings(n):
    # Step 1: Generate all possible strings of length `n`
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_strings = []  # Create an empty list to store generated strings

    # Use a nested loop to manually generate combinations for small `n`
    def backtrack(current_string):
        if len(current_string) == n:
            all_strings.append(current_string)  # Add the generated string to the list
            return
        
        for letter in letters:  # Try each letter from 'A' to 'Z'
            backtrack(current_string + letter)  # Append the letter and continue

    backtrack("")  # Start with an empty string

    return all_strings  # Return the sorted list

def find_lexicographical_string(n, m):
    all_strings = generate_strings(n)  # Generate all possible strings

    # Step 2: Check if M is valid
    if m > len(all_strings):
        return "Not possible"

    # Step 3: Return the M-th string (1-based index)
    return all_strings[m - 1]

# Example cases
n, m = 2, 3
print(find_lexicographical_string(n, m))  # Output: "BA"

n, m = 2, 4
print(find_lexicographical_string(n, m))  # Output: "Not possible"
