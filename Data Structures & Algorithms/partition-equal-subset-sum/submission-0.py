class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        half = s / 2

        n = len(nums)
        memo = {}

        def dfs(i, curSum):
            if curSum == half:
                return True
            if i == n:
                return False
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            #include it or dont in the subset
            if dfs(i+1, curSum+nums[i]) or dfs(i+1, curSum):
                return True

            memo[(i, curSum)] = False
            return False
        
        return dfs(0, 0)

        