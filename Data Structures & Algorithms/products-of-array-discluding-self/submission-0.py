class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]

        prefix_total = 1
        suffix_total = 1

        for i in range(1, len(nums), 1):
            prefix_total *= nums[i-1]
            prefix[i] = prefix_total

        for i in range(len(nums) - 2, -1, -1):
            suffix_total *= nums[i+1]
            suffix[i] = suffix_total
    
        for i in range(len(result)):
            result[i] = prefix[i]*suffix[i]

        return result
            