'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l = buy day, r = sell day
        maxp = 0  # max profit we’ve seen so far

        while r < len(prices):  # keep going until the end of the list
            # If the selling price is higher than the buying price
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]  # calculate profit
                maxp = max(maxp, profit)  # update max profit if this profit is bigger
            else:
                l = r  # move the buy day to the sell day
            r += 1  # move the sell day to the next day

        return maxp

#OR
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start with the highest possible value for min_price
        # So any price in the list will be smaller and replace it
        min_price = float('inf')  # Think of this as "infinity"

        # Start with zero profit — we haven’t bought/sold anything yet
        max_profit = 0

        # Go through each price in the list
        for price in prices:
            if price < min_price:
                # Found a new lower price — update our "buy" price
                min_price = price
            else:
                # Price is higher than what we've seen — this could be a sell day
                # Calculate potential profit: sell - buy
                profit = price - min_price

                # Keep track of the highest profit we've seen
                max_profit = max(max_profit, profit)

        # After checking all days, return the best profit found
        return max_profit
