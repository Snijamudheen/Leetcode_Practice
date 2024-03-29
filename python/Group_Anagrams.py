'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charcount to list of anagrams

        for s in strs:
            count = [0] * 26 # counting a to z, initializing all chars to 0

            for c in s:
                count[ord(c) - ord("a")] += 1 # counting each char, a is in index 0 and z in index 25

            res[tuple(count)].append(s) # group the results together, lists cannot be keys so use tuple

        return res.values()  # we only need values not keys
