'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Create an empty stack
        CloseToOpen = {")": "(", "]": "[", "}": "{"}  # Mapping of closing brackets to their open counterparts

        for c in s:  # Loop through each character in the string
            if c in CloseToOpen:  # If it's a closing bracket
                if stack and stack[-1] == CloseToOpen[c]:  # Check if the top of the stack matches the corresponding open bracket
                    stack.pop()  # If it matches, remove the top element from the stack
                else:
                    return False  # If it doesn't match, return False
            else:  # If it's an open bracket
                stack.append(c)  # Push it onto the stack

        return True if not stack else False  # Return True if the stack is empty at the end, otherwise False

''' c = '{'
It's not in the CloseToOpen dictionary, which means it's an open bracket.
Action: Push it onto the stack.

c = ')'
It's a closing bracket, so we check if it matches the top of the stack.
The top of the stack is '('.
According to the CloseToOpen dictionary, the matching open bracket for ) is '('.
✅ Match!

Action: Pop the top of the stack.
'''
