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
