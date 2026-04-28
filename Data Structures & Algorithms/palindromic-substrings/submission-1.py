class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # Odd-length: center at i, start with l=r=i
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            # Even-length: center between i and i+1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count
        