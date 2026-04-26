class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        n = len(candidates)
        res, sol = [], []
        sum = 0

        def backtrack(i):
            nonlocal sum
            if sum == target:
                res.append(sol[:])
                return
            if sum > target or i == n:
                return
            
            # skip candidates[i] (and all its duplicates)
            j = i + 1
            while j < n and candidates[j] == candidates[i]:
                j += 1
            backtrack(j)
            
            # pick candidates[i] — at most once, so advance to i+1
            sol.append(candidates[i])
            sum += candidates[i]
            backtrack(i+1)
            sol.pop()
            sum -= candidates[i]


        backtrack(0)
        return res
        