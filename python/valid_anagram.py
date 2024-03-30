'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts, countt = {}, {}

        for i in range (len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)
        
        for c in counts:
            if counts[c] != countt.get(c,0):
                return False
        
        return True
