class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()
        n = len(s)

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            length = (r - l) + 1
            longest = max(longest, length)
            seen.add(s[r])

        return longest