# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Step 1: Get the lengths of both strings
        rows = len(text1) + 1  # Number of rows in the dp table plus the extra row for out of bounds with zeroes
        cols = len(text2) + 1  # Number of columns in the dp table plus the extra col for out of bounds with zeroes

        # Step 2: Create an empty dp table with all zeros
        dp = []  # This will hold our table
        for i in range(rows):
            dp.append([0] * cols) # It ensures that each row in the dp table has the same number of columns as text2 (plus one extra column for the empty string case).

        # Step 3: Loop through both strings from the end to the beginning
        # We go backward to fill the table bottom-up.
        for i in range(len(text1) - 1, -1, -1):  # Loop through text1 backwards
            for j in range(len(text2) - 1, -1, -1):  # Loop through text2 backwards
                # Step 3: If the characters match, add 1 to the result from the diagonal cell
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # Step 4: If the characters don't match, take the maximum of the right cell or the bottom cell
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # Step 5: The answer is in the top-left cell of the dp table
        return dp[0][0]
