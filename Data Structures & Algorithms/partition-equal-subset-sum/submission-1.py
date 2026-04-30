class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Top Down
        # s = sum(nums)
        # if s % 2 == 1:
        #     return False
        # half = s / 2

        # n = len(nums)
        # memo = {}

        # def dfs(i, curSum):
        #     if curSum == half:
        #         return True
        #     if i == n:
        #         return False
        #     if (i, curSum) in memo:
        #         return memo[(i, curSum)]

        #     #include it or dont in the subset
        #     if dfs(i+1, curSum+nums[i]) or dfs(i+1, curSum):
        #         return True

        #     memo[(i, curSum)] = False
        #     return False
        
        # return dfs(0, 0)

        s = sum(nums)
        if s % 2 == 1:
            return False
        half = s // 2

        # dp holds all sums reachable using the elements seen so far.
        dp = set()
        dp.add(0)

        for n in nums:
            nextDp = set()
            for cur in dp:
                nextDp.add(cur + n)
                nextDp.add(cur)
            dp = nextDp

        return half in dp

        