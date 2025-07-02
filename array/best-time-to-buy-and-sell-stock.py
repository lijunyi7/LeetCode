class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            # Update max profit if we sell today
            profit = price - min_price
            max_profit = max(max_profit, profit)
            
            # Update min price if we find a cheaper one
            min_price = min(min_price, price)
        
        return max_profit


        