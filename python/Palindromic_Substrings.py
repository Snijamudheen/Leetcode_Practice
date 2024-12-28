# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        #odd substrings, pointer in the first elemen
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

        return res


# OR

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l = r = i
            res += self.countpalin(s, l, r)

            l = i
            r = i + 1
            res += self.countpalin(s, l, r)

        return res

    def countpalin(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            res += 1
        return res

# OR (best), just substituted l and r in countpalin func call

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countpalin(s, i, i)
            res += self.countpalin(s, i, i + 1)

        return res

    def countpalin(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            res += 1
        return res


 
