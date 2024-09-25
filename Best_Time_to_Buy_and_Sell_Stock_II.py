class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0

        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit

        return max_profit
