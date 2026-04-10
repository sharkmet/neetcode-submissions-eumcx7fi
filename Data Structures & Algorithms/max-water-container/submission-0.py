class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        vol_max = 0

        while l < r:
            volume = (r-l)*min(heights[l], heights[r])
            if volume >= vol_max:
                vol_max = volume
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return vol_max