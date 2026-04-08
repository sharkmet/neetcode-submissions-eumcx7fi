class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Use result to store prefix products
        prefix_total = 1
        for i in range(1, n):
            prefix_total *= nums[i-1]
            result[i] = prefix_total

        # Multiply suffix products directly into result
        suffix_total = 1
        for i in range(n - 2, -1, -1):
            suffix_total *= nums[i+1]
            result[i] *= suffix_total

        return result
            