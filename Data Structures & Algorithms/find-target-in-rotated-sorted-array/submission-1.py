class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # decide which half to search
        if target <= nums[-1]:
            l, r = l, len(nums) - 1  # search right half
        else:
            l, r = 0, l - 1          # search left half

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid

        return -1