class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR is commutative and associative, same number xor is zero, zero and a number is the number
        res = 0
        for num in nums:
            res ^= num
        return res

        