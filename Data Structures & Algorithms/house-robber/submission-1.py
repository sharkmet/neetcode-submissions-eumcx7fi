class Solution:
    def rob(self, nums: List[int]) -> int:
        #Bottom Up
        # n = len(nums)
        # dp = [0] * (n+2)
        
        # for i in range(n-1, -1, -1):
        #     dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        # return dp[0]

        prev, curr = 0, 0
        for n in reversed(nums):
            prev, curr = curr, max(n + prev, curr)
        return curr
        