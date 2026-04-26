class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        sum = 0

        def backtrack(i):
            nonlocal sum
            if sum == target:
                res.append(sol[:])
                return
            if sum > target or i == n:
                return
            
            # skip nums[i]
            backtrack(i+1)
            
            # pick nums[i] — stay at i for reuse
            sol.append(nums[i])
            sum += nums[i]
            backtrack(i)
            sol.pop()
            sum -= nums[i]


        backtrack(0)
        return res


        