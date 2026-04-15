class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        n = len(prices)
        min_l = 100

        for i in range(n):
            profit = prices[i] - min_l
            max_profit = max(max_profit, profit)

            if prices[i] < min_l:
                min_l = prices[i]

        return max_profit
            

        