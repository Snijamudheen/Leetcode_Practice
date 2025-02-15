# reverse a string and capitalize the front and end letter of the word

def reverse_and_capitalize(s: str) -> str:
    # Reverse the string using slicing.
    # Slicing syntax: sequence[start:stop:step]
    # In s[::-1]:
    # - 'start' is omitted, so it starts from the beginning of the string.
    # - 'stop' is omitted, so it goes all the way to the end.
    # - 'step' is -1, which means it steps through the string backwards.
    # This effectively reverses the string.
    rev = s[::-1]
    
    # If the reversed string is empty, just return it.
    if len(rev) == 0:
        return rev
    
    # If the string has only one character, simply return it in uppercase.
    if len(rev) == 1:
        return rev.upper()
    
    # The next line constructs the final string by:
    # 1. rev[0].upper() - Taking the first character of the reversed string and capitalizing it.
    # 2. rev[1:-1]    - Taking the substring that excludes the first and last characters.
    # 3. rev[-1].upper() - Taking the last character of the reversed string and capitalizing it.
    # The '+' operator concatenates these three parts.
    return rev[0].upper() + rev[1:-1] + rev[-1].upper()

# Example usage:
if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = reverse_and_capitalize(user_input)
    print("Result:", result)
