class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        #Forwards
        prev1, curr1 = 0, 0
        for n in nums1:
            prev1, curr1 = curr1, max(prev1 + n, curr1)
        
        prev2, curr2 = 0, 0
        for n in nums2:
            prev2, curr2 = curr2, max(prev2 + n, curr2)

        return max(curr1, curr2)

        