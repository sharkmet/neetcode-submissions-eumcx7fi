class Solution:
    def numDecodings(self, s: str) -> int:
        # # Memoization
        # memo = {}

        # def dfs(i):
        #     # Base case 1: reached the end successfully
        #     if i == len(s):
        #         return 1
        #     # Base case 2: leading zero, dead end
        #     if s[i] == '0':
        #         return 0
        #     # Memo hit
        #     if i in memo:
        #         return memo[i]
            
        #     # Choice 1: take one digit
        #     res = dfs(i + 1)
            
        #     # Choice 2: take two digits (if valid and in bounds)
        #     if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
        #         res += dfs(i + 2)
            
        #     memo[i] = res
        #     return res
        
        # return dfs(0)

        # Bottom Up - dp
        # n = len(s)
        # dp = [0] * (n + 1)
        # dp[n] = 1  # base case: empty string has 1 way
        
        # for i in range(n - 1, -1, -1):
        #     if s[i] == '0':
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]
        #         if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
        #             dp[i] += dp[i + 2]
        
        # return dp[0]

        n = len(s)
        dp1, dp2 = 1, 0  # dp1 = dp[i+1], dp2 = dp[i+2]
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = dp1
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    cur += dp2
            
            dp2 = dp1
            dp1 = cur
        
        return dp1

        