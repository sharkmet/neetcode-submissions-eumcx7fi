class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i]) -1
            if nums[idx] < 0:
                return abs(nums[i])
            nums[idx] *= -1

            

        