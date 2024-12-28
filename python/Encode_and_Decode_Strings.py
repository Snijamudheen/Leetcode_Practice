# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.Please implement encode and decode

class Solution:

    def encode(self, strs):
        res = ""

        # result = Add length + "#" + word
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str):
        res = []
        i = 0 

        #Loop until we've processed the entire encoded string
        while i < len(str):
            # `j` is another pointer used to find the position of "#"
            j = i

            # Move `j` forward until we find the "#"
            # This tells us where the length of the next string ends
            while str[j] != "#":
                j += 1
            
            # Extract the substring from `i` to `j` (before the "#") and convert it to an integer
            # This integer represents the length of the next word
            length = int(str[i:j])

            # Extract the actual word using `j + 1` (start of the word) and `j + 1 + length` (end of the word)
            res.append(str[j + 1 : j + 1 + length])

            # Move `i` to the next segment: skip over the length, the "#" symbol, and the extracted word. Basically we checking the second string
            i = j + 1 + length

        return res
