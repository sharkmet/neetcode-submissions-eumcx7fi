class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l) // 2

            if (nums[mid] > nums[r]): #minimum is in the right half 
                l = mid + 1
            else: #left half 
                r = mid
   
        return nums[l]

        