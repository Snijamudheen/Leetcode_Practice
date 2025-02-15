'''Populate an array of numbers from 1 to N (inclusive). Given two numbers, p and q , 
if a number in the array is divisible by p print OUT if a number is divisible by q print THINK. If the number is divisible by both p and q, print OUTTHINK'''

def outthink_numbers(n, p, q):
    # Create an array (list) of numbers from 1 to n (inclusive)
    numbers = list(range(1, n + 1))
    
    # Loop over each number in the list
    for num in numbers:
        # Check if the number is divisible by both p and q first
        if num % p == 0 and num % q == 0:
            print("OUTTHINK")
        # If not, check if it's divisible by p only
        elif num % p == 0:
            print("OUT")
        # Check if it's divisible by q only
        elif num % q == 0:
            print("THINK")
        # If none of the above, print the number itself
        else:
            print(num)

# Example usage:
if __name__ == "__main__":
    N = int(input("Enter N: "))
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    outthink_numbers(N, p, q)
