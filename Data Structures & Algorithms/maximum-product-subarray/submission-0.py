class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = curMax = 1
        
        for n in nums:
            if n == 0:
                curMin = curMax = 1
                continue
            
            tmp = curMax * n
            curMax = max(n, curMax * n, curMin * n) #Start best, extend current best, or flip a neg and it extends into new best
            curMin = min(n, tmp, curMin * n)
            
            res = max(res, curMax)
        
        return res