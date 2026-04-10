class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        result = 0

        pre_max = height[0]
        for i in range(1, len(height)):
            pre_max = max(pre_max, height[i])
            prefix[i] = pre_max
            
        suff_max = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            suff_max = max(suff_max, height[i])
            suffix[i] = suff_max
            
        for i in range(1, len(height)-1):
            result += (min(prefix[i], suffix[i])-height[i])
        
        return result