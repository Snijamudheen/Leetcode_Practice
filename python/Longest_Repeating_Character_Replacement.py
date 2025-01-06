# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    # Function to find the longest substring with the same letter after making at most k changes
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the variable to store the longest valid substring length
        longest = 0

        # Left pointer for the sliding window
        l = 0

        # Array to count the frequency of each letter in the current window
        # There are 26 letters in the alphabet, so we initialize an array of size 26
        counts = [0] * 26

        # Iterate over the string with the right pointer (r)
        for r in range(len(s)):
            # Increase the count of the current letter in the window by moving right pointer
            # We use ord(s[r]) to convert the letter to its ASCII value and subtract 65 to get its index (A=0, B=1, ..., Z=25)
            counts[ord(s[r]) - 65] += 1

            # Check if the current window size is valid
            # (r - l + 1) is the size of the window
            # max(counts) gives the highest frequency of any letter in the window
            # If the difference between the window size and the highest frequency letter is more than k, it means
            # we need to make more than k changes which is not allowed, so the window is not valid
            while (r - l + 1) - max(counts) > k: # not valid
                counts[ord(s[l]) - 65] -= 1 # remove the character from the left
                l += 1 # shrink the window from the left by moving left pointer to thr right so +=

            # Update the longest valid substring length
            longest = max(longest, (r - l + 1))

        # Return the length of the longest valid substring
        return longest
