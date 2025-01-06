# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # This is a Dynamic Programming (DP) problem.
        # Our goal is to figure out the fewest number of coins
        # needed to make the `amount` using the given `coins`.

        # Step 1: Sort the coins in ascending order
        # Sorting helps us stop checking coins once we find one that's too big.
        coins.sort()

        # Step 2: Create a DP table where dp[i] represents
        # the minimum number of coins needed to make amount `i`.
        # We start by initializing the table with zeros.
        # dp[0] = 0 because to make amount 0, we need 0 coins.
        dp = [0] * (amount + 1)

        # Step 3: Fill the DP table from 1 to `amount + 1`.
        # Start at 1 because we already know dp[0] = 0.
        for i in range(1, amount + 1):
            # Set a variable `minn` to keep track of the minimum number of coins needed for amount `i`.
            # Since we don’t know if the sum can be formed yet, start with infinity.
            minn = float('inf')

            # Step 4: Check each coin to see if we can use it to make the current amount `i`.
            for coin in coins:
                # Calculate the remaining amount after using this coin.
                # `i` is the current amount we are trying to make,
                # and `coin` is the coin value we are considering.
                diff = i - coin

                # If the remaining amount is negative, it means this coin is too big.
                # Stop checking further coins.
                if diff < 0:
                    break

                # Update `minn` to be the minimum number of coins needed for the current amount `i`.
                # We compare the current `minn` with the number of coins needed to make the remaining amount (`dp[diff]`) plus one more coin (the current coin we're using).
                minn = min(minn, dp[diff] + 1)

            # Update the DP table for the current amount `i` with the minimum number of coins found.
            dp[i] = minn

        # Step 5: Check if we were able to make the target `amount` using the given coins.
        # If `dp[amount]` is still `float('inf')`, it means we couldn’t make that amount, so return -1.
        # Otherwise, return `dp[amount]`, which is the minimum number of coins needed.
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
