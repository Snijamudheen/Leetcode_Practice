'''You are given a string word and an array of strings forbidden.

A string is called valid if none of its substrings are present in forbidden.

Return the length of the longest valid substring of the string word.

A substring is a contiguous sequence of characters in a string, possibly empty.'''

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        max_len = 0
        prev = 0  # valid length ending at previous character

        for i in range(len(word)):
            curr = i + 1  # assume everything from 0 to i is valid

            # Only check last 10 characters ending at i
            for j in range(10):
                if i - j < 0:
                    break

                if word[i - j: i + 1] in forbidden_set:
                    # We found a bad substring of length (j+1)
                    curr = j
                    break

            # curr can't grow more than +1 from prev
            curr = min(curr, prev + 1)

            max_len = max(max_len, curr)
            prev = curr  # save for next loop

        return max_len
