class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        set_num = set(nums)

        for num in set_num:
            if num-1 not in set_num:
                count = 1
                while num+count in set_num:
                    count += 1
                result=max(result, count)
        return result