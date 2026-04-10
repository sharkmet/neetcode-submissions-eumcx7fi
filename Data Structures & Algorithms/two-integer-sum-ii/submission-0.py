class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        indicies = []

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                indicies.append(l+1)
                indicies.append(r+1)
                return indicies
            if s > target:
                r -= 1
            if s < target:
                l += 1

