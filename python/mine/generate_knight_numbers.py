# code to determine all possible telephone numbers from a mobile keypad in a situation where every digit can only make knight moves on the keypad.

def generate_knight_numbers(n):
    # Step 1: Define the valid knight moves.
    # This dictionary tells you which digits you can jump to from each digit.
    moves = {
        '0': ['4', '6'],
        '1': ['6', '8'],
        '2': ['7', '9'],
        '3': ['4', '8'],
        '4': ['0', '3', '9'],
        '5': [],      # '5' cannot move anywhere.
        '6': ['0', '1', '7'],
        '7': ['2', '6'],
        '8': ['1', '3'],
        '9': ['2', '4']
    }
    
    results = []  # This list will store all the complete phone numbers we create.
    
    # Step 2: Define a helper function using recursion.
    # "path" is the phone number built so far.
    # "remaining" is the number of digits we still need to add.
    def dfs(path, remaining):
        # If no more digits are needed, we have a complete phone number.
        if remaining == 0:
            results.append(path)
        else:
            # Get the last digit in our current number.
            last_digit = path[-1]
            # For every valid knight move from this digit:
            for next_digit in moves[last_digit]:
                # Add the new digit to our path and decrease the remaining count by 1.
                dfs(path + next_digit, remaining - 1)
    
    # Step 3: Start the recursion from each digit on the keypad.
    # Each digit becomes a starting point for a phone number.
    for digit in moves.keys():
        dfs(digit, n - 1)  # We already have one digit, so we need n-1 more.
    
    return results

# Example usage:
if __name__ == "__main__":
    length = int(input("Enter telephone number length: "))
    numbers = generate_knight_numbers(length)
    print("Possible telephone numbers:")
    for num in numbers:
        print(num)
