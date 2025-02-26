# check if a string is in alphabetical order and return either 0 or the index where it goes out of order

def check_alphabetical_order(inputString):
    for i in range(1, len(inputString)):
        if inputString[i] < inputString[i - 1]:
            print(i)
            return
    print(0)

# Example usage
inputString = input("Enter a string: ")
check_alphabetical_order(inputString)
