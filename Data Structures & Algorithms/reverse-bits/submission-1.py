class Solution:
    def reverseBits(self, n: int) -> int:
        # res= 0
        # for i in range(32):
        #     bit = ((n >> i) & 1)
        #     res |= (bit << (31 - i))

        # return res

        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result
