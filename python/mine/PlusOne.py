'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right 
order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit (rightmost) and move left
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is 9, it will become 10 when we add 1
            # So we set it to 0 and carry the 1 to the next digit
            if digits[i] == 9:
                digits[i] = 0  # Turn this digit into 0 (because 9 + 1 = 10, so carry the 1)
            else:
                # If the digit is not 9, just add 1 and return the result
                # No more carry needed, so we can return immediately
                digits[i] += 1
                return digits
        
        # If we finished the loop and all digits were 9 (like 999 → 1000),
        # we need to add a new 1 at the front of the array
        return [1] + digits

# 🧪 Example Walkthrough for Input [1, 2, 9]:
# Step 1: Start with the last digit (9). Set it to 0 and carry the 1.
#         Array becomes [1, 2, 0].
# Step 2: Move to the next digit (2). Add 1 to it. Array becomes [1, 3, 0].
# Step 3: Return the final array [1, 3, 0].

# 🧪 Example Walkthrough for Input [9, 9, 9]:
# Step 1: Start with the last digit (9). Set it to 0 and carry the 1.
#         Array becomes [9, 9, 0].
# Step 2: Move to the next digit (9). Set it to 0 and carry the 1.
#         Array becomes [9, 0, 0].
# Step 3: Move to the first digit (9). Set it to 0 and carry the 1.
#         Array becomes [0, 0, 0].
# Step 4: Since all digits are now 0, we need to add a new 1 at the front.
#         Final array becomes [1, 0, 0, 0].
