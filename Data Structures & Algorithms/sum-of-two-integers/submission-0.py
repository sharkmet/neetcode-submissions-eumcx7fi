class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            bit1 = a & 1
            bit2 = b & 1
            bit = bit1 ^ bit2 ^ carry

            if (bit1 == 1 and bit2 == 1) or (bit1 == 1 and carry == 1) or (bit2 == 1 and carry == 1):
                carry = 1
            else:
                carry = 0

            res |= bit << i

            a >>= 1
            b >>= 1

        if res >= (1 << 31):
            res = ~(res ^ 0xFFFFFFFF)
            #res ^ 0xFFFFFFFF flips all 32 bits.
            #~x in Python gives -x - 1.

        return res
        