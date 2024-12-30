# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'
# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").
# For example, "11106" can be decoded into:
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.
# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.
# The test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
    def numDecodings(self, s: str) -> int:
        # If the string starts with '0', it cannot be decoded
        if s[0] == "0":
            return 0

        # Initialize DP array to handle the number of ways to decode
        # dp[i] stores the number of ways to decode the string up to the i-th character
        dp = [1, 1]  # dp[0] and dp[1] are initialized to 1

        # Iterate through the string starting from the second character
        for index, num in enumerate(s[1:], 2):
            # Initialize the number of ways to decode at the current position
            ways = 0
            
            # If the current digit is not '0', it can be decoded as a single character
            if num != "0":
                ways += dp[index - 1]
            
            # If the last two digits form a number between 10 and 26, decode it as a double character
            if 10 <= int(s[index - 2] + num) <= 26:
                ways += dp[index - 2]
            
            # Update the DP array with the number of ways at the current position
            dp.append(ways)
        
        # Return the total number of ways to decode the full string
        return dp[-1]
