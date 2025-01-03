# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        # Create a dictionary to store the already known results (base cases):
        # - 1 step: 1 way to climb
        # - 2 steps: 2 ways to climb (1+1 or 2)
        memo = {1: 1, 2: 2}

        # Define a helper function to calculate the number of ways to climb `n` steps
        def f(n):
            # If we've already solved this problem (it's in the memo), just return the saved answer
            if n in memo:
                return memo[n]
            else:
                # If we haven't solved it, calculate it:
                # Number of ways to climb `n` steps is:
                #   ways to climb `n-1` steps + ways to climb `n-2` steps
                memo[n] = f(n - 2) + f(n - 1)
                return memo[n]  # Return the result after storing it in `memo`

        # Start the calculation for `n` steps
        return f(n)
