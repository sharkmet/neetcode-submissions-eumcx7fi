class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                l = len(word)
                if s[i:i+l] == word:
                    if dfs(i+l): # if this path succeeds, return immediately
                        return True
            
            memo[i] = False
            return False 
 
        return dfs(0)
            




            

        