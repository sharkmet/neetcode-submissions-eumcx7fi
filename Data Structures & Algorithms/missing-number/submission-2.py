class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Using XOR property
        n = len(nums)
        res = 0
        for i in range(n+1):
            res ^= i
        for num in nums:
            res ^= num
        return res


        #Sum Toal - Actual Solution rearranged
        # # [0, 1, 2, 3]
        # # [0, 1, 3]
        
        # # total - nums sum
        # res = len(nums)
        # n = len(nums)
        # for i in range(n):
        #     res += i - nums[i]
        
        # return res
        