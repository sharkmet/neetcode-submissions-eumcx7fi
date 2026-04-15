class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_l = float('inf')

        for i in range(len(prices)):
            profit = prices[i] - min_l
            max_profit = max(max_profit, profit)

            if prices[i] < min_l:
                min_l = prices[i]

        return max_profit
            

        