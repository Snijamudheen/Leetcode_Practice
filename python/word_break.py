# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the word dictionary to a set for faster lookups
        wordDict = set(wordDict)

        # Initialize variables
        n = len(s) + 1  # Length of the string plus one for DP indexing
        dp = [False] * n  # DP array to track if s[:i] can be segmented, dp = [False, False, False, False, False, False, False, False, False]
        dp[0] = True  # Base case: an empty string can always be segmented, dp = [True, False, False, False, False, False, False, False, False]
        trues = [0]  # Indices where dp[i] is True (starting with 0)

        # Iterate through each index of the string starting at 1 since index 0 has nothing since it is the start of the string
        for i in range(1, n):
            # Check all previous True indices in the trues dp array
            for j in trues:
                # If the substring from index j to i is in the dictionary
                if s[j:i] in wordDict:
                    dp[i] = True  # Mark dp[i] as True since it can be segmented
                    trues.append(i)  # Add the index i to the list of True indices
                    break  # No need to check further for this i, break out of the loop
            
        # Return whether the entire string can be segmented, By the end of the loop(last element), dp[-1] will hold the result for s[:len(s)] (i.e., the whole string s).
        return dp[-1]
