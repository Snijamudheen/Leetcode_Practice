# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # This will store all the valid combinations
        res = []

        # Define a recursive helper function to explore all combinations
        def dfs(i, cur, total):
            # If the total is exactly equal to the target, we found a valid combination
            if total == target:
                res.append(cur.copy())  # Add a copy of the current combination to the results
                return  # End this branch of recursion
            
            # If we've used all candidates or the total exceeds the target, stop exploring this path
            if i >= len(candidates) or total > target:
                return
            
            # Include the current candidate in the combination
            cur.append(candidates[i])  # Add the current candidate to the list
            dfs(i, cur, total + candidates[i])  # Call dfs with the same index to allow reuse of the candidate
            cur.pop()  # Backtrack by removing the last candidate added so we can add new numbers like 2,2,3 (removed the last 2 from 2,2,2 and put 3 instead)
            
            # Skip the current candidate and move to the next one, we exhausted 2 so lets never use 2 and move on to the next value so i + 1
            dfs(i + 1, cur, total)

        # Start the depth-first search (dfs) with the first candidate, an empty combination, and a total of 0
        dfs(0, [], 0)
        
        # Return the list of all valid combinations
        return res
