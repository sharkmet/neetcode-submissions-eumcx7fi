class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # #Top Down
        # n = len(s)
        # memo = {}

        # def dfs(i):
        #     if i == n:
        #         return True
        #     if i in memo:
        #         return memo[i]
            
        #     for word in wordDict:
        #         l = len(word)
        #         if s[i:i+l] == word:
        #             if dfs(i+l): # if this path succeeds, return immediately
        #                 return True
            
        #     memo[i] = False
        #     return False 
 
        # return dfs(0)

        #Bottom Up
        n = len(s)
        dp = [False] * (n + 1) #dp[i] means "can the substring s[i:] be segmented
        dp[n] = True # reaching the end means we successfully segmented

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                l = len(word)
                if s[i:i+l] == word and dp[i+l]:
                    dp[i] = True
                    break

        return dp[0]
            




            

        