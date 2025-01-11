'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the two strings are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # Create two empty dictionaries to count the characters in both strings
        counts, countt = {}, {}

        # Loop through each character in both strings
        for i in range(len(s)):
            # For string 's', increase the count of the character by 1
            # If the character doesn't exist in the dictionary, start with 0
            # dictionary.get(key, default_value)
            counts[s[i]] = 1 + counts.get(s[i], 0)

            # For string 't', do the same
            countt[t[i]] = 1 + countt.get(t[i], 0)

        # Now compare the character counts in both dictionaries
        for c in counts:
            # If a character's count in 's' doesn't match its count in 't', return False
            # If the key c does not exist in the countt dictionary, using countt[c] will raise a KeyError.
            # Using .get(c, 0) ensures that if c isn’t found in countt, it will return 0 instead of throwing an error.
            if counts[c] != countt.get(c, 0):
                return False

        # If all character counts match, return True
        return True
