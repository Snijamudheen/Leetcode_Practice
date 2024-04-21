'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in CloseToOpen:
                if stack and stack [-1] == CloseToOpen[c]: #if value in stack and value on top of stack matches then pop or delete the two, when it starts with a closing bracket
                    stack.pop()
                else: 
                    return False
            else: #if it starts with opening bracket, then we can keep adding whatever comes after
                stack.append(c)

        return True if not stack else False #stack shud be empty at the end, if not its not matching
        
