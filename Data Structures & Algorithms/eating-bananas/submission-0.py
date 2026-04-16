class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        result = r # max(piles) always works, so it's a safe default

        while l <= r:
            k = l + (r - l) // 2
            time = 0
            for p in piles:
                time += (p + k -1) // k # math.ceil(p / k)

            if time <= h: # k works, try smaller
                result = k
                r = k - 1
            else: # k too slow, need bigger
                l = k + 1

        return result

        