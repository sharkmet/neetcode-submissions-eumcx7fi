class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # #Top Down
        # memo = {}

        # def dfs(remaining): #"What is the minimum number of coins needed to make exactly remaining amount?"
        #     if remaining == 0: #If remaining amount is 0, you need 0 coins. Done.
        #         return 0
        #     if remaining < 0: #You overshot — this path is invalid. 
        #         return float('inf')
        #     if remaining in memo:
        #         return memo[remaining]

        #     best = float('inf')
        #     #"If I use this coin, how many coins does the remaining amount need?"
        #     for coin in coins:
        #         result = dfs(remaining - coin)
        #         best = min(best, 1 + result) #"Is this coin's result better than the best I've seen so far?"

        #     memo[remaining] = best
        #     return best
        
        # ans = dfs(amount)
        # return ans if ans != float('inf') else -1
        
        #Bottom Up
        dp = [float('inf')] * (amount + 1) #"minimum coins to make amount i"
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin]) #min coins for the leftover amount after using this coin -> dp[i-coin]

        return dp[amount] if dp[amount] != float('inf') else -1