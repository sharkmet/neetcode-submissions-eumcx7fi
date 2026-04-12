class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i # how far left can this bar extend?

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height *(i - idx))
                start = idx # current bar can extend back to here

            stack.append((start, h))

        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
    
        return max_area