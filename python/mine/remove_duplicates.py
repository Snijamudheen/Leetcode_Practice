# remove duplicate characters from a string while preserving the order of their first occurrence.

def remove_duplicates(s):
    result = ""   # This will store our result without duplicates.
    seen = set()  # This set keeps track of characters we've already encountered.
    
    # Loop through each character in the string.
    for char in s:
        # If the character hasn't been seen before, add it to our result and mark it as seen.
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Example usage:
input_str = "banana"
print(remove_duplicates(input_str))  # Output: "ban"
