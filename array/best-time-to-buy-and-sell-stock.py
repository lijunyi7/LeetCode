class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        spend = min(prices)
        profit = -spend
        max_profit = 0
        for i in range(prices.index(spend) + 1, len(prices)):
            max_profit = max(max_profit, prices[i] + profit)
        return max_profit

        