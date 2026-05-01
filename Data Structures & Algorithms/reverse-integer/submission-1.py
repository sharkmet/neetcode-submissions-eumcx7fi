class Solution:
    def reverse(self, x: int) -> int:
        # MAX = 2**31 - 1      # 2147483647
        # MIN = -2**31         # -2147483648
        # res = 0

        # while x != 0:
        #     # extract last digit (careful with negatives — see note below)
        #     digit = int(math.fmod(x, 10))   # gives remainder -9..9, sign matches x
        #     x = int(x / 10) if x < 0 else x // 10  # truncate toward 0

        #     # overflow checks
        #     if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
        #         return 0
        #     if res < -(-MIN // 10) or (res == -(-MIN // 10) and digit < -(-MIN % 10)):
        #         return 0

        #     res = res * 10 + digit

        # return res


        #Cleaner Version
        MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            res = res * 10 + digit

        return sign * res