class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top Down - Memo
        # n = len(cost)
        # memo = {}

        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     # pay this stair's toll, then take the cheaper of the two jumps
        #     memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return memo[i]

        # return min(dfs(0), dfs(1))

        #Bottom Up array
        # n = len(cost)
        # dp = [0] * (n + 2)        # dp[n] and dp[n+1] are 0 (at the top)
        
        # for i in range(n - 1, -1, -1):       # iterate backwards
        #     dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        # return min(dp[0], dp[1])

        #Bottom Up
        n = len(cost)
        one_ahead, two_ahead = 0, 0 # position n and n+1 already there so 0
        for i in range(len(cost) - 1, -1, -1):
            one_ahead, two_ahead = cost[i] + min(one_ahead, two_ahead), one_ahead
        return min(one_ahead, two_ahead)
            



        