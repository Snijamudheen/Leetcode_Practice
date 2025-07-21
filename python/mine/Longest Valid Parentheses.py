'''Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # We use this to keep track of indices. Start with -1 to handle edge cases.
        max_len = 0   # This will store the length of the longest valid parentheses so far.

        # Go through each character in the string
        for i in range(len(s)):
            if s[i] == "(":       # If it's an opening bracket
                stack.append(i)   # Save its index on the stack
            else:                 # If it's a closing bracket
                stack.pop()       # Try to match it with an opening bracket
                
                if len(stack) == 0:
                    # No opening bracket to match it — reset base index
                    stack.append(i)
                else:
                    # Valid pair found — calculate length from last unmatched '('
                    current_len = i - stack[-1]
                    max_len = max(max_len, current_len)

        return max_len  # Return the longest valid parentheses length
