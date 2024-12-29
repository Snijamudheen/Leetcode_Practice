# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""

      # check if every character in string is an alphanumerical value, if it is then add it to the new string and make it lowercase so we can compare 
        for c in s:
            if c.isalnum():
                newstr += c.lower()

        # compare new string and reverse string (read from backwards and compare first and last letter to see if palindrome)
        return newstr == newstr[::-1]

# OR

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # left pointer on first element, right on the last element

        # shud not go out of bounds, Skip Non-Alphanumeric Characters
        while l < r:
            while l < r and not self.alphanum(s[l]): # shud not go out of bounds and if its not alphanum then skip and go to next letter (left)
                l += 1
            while r > l and not self.alphanum(s[r]): # shud not go out of bounds and if its not alphanum then skip and go to next letter (right)
                r -= 1
            if s[l].lower() != s[r].lower(): # if the letters are not equal then not a plaindrome so false. compare in lowercase
                return False
            l, r = l + 1, r - 1 # if they are equal charcters then keep moving
        
        return True

    # makes sure each character in string is aplhanumerical and it lies between A to Z or a to z or 0 to 9
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        
