class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) 
        dp = [1] * n  # every element is a subsequence of length 1 by itself
        # dp[i] = length of longest increasing subsequence ending at index i.

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp) #dp[i] means the LIS must end at i, so the global answer could be at any position.

        # #Top down
        # memo = {}

        # def dfs(i, j):
        #     if i == len(nums):
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     # skip nums[i]
        #     res = dfs(i + 1, j)

        #     # include nums[i] if it's greater than previous
        #     if j == -1 or nums[i] > nums[j]:
        #         res = max(res, 1 + dfs(i + 1, i))

        #     memo[(i, j)] = res
        #     return res

        # return dfs(0, -1)
