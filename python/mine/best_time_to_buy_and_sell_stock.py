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
