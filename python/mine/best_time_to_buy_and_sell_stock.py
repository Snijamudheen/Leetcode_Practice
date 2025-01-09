'''You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # Try every possible pair of days
        for buy_day in range(len(prices)):
            for sell_day in range(buy_day + 1, len(prices)):
                # Calculate profit if you buy on 'buy_day' and sell on 'sell_day'
                profit = prices[sell_day] - prices[buy_day]

                # Update max_profit if this profit is bigger
                if profit > max_profit:
                    max_profit = profit

        return max_profit
