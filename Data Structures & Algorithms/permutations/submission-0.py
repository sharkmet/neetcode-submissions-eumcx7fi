class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        used = [False] * n # used[j] tells you whether nums[j] is currently sitting in sol
        
        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for j in range(n):
                if used[j]:
                    continue
                
                sol.append(nums[j])
                used[j] = True
                backtrack()
                sol.pop()
                used[j] = False
        
        backtrack()
        return res


        