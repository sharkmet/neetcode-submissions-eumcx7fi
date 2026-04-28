class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen, res = 0, 0
        
        for i in range(len(s)):
            # Odd-length: center at i, start with l=r=i
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = l
                l -= 1
                r += 1
            
            # Even-length: center between i and i+1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = l
                l -= 1
                r += 1
        
        return s[res : res + resLen]

            
