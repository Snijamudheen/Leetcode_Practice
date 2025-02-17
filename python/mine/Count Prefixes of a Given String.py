'''You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.
Return the number of strings in words that are a prefix of s.
A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.'''

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0  # Start with 0 because we haven't counted anything yet

        for i in words:  # Go through each word in the list
            if i == s[:len(i)]:  # Check if the word matches the beginning of s
                count += 1  # If it does, add 1 to our count

        return count  # Give back the total number of prefixes found
