class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        s_freq = {}
        l = 0
        shortest = None

        def valid():
            for key in t_freq:
                if s_freq.get(key, 0) < t_freq[key]:
                    return False
            return True

        for r in range(len(s)):
            s_freq[s[r]] = s_freq.get(s[r], 0) + 1


            while valid():
                if shortest is None or len(s[l:r+1]) < len(shortest):
                    shortest = s[l:r+1]

                if s_freq[s[l]] == 1:
                    del s_freq[s[l]]
                else:
                    s_freq[s[l]] -= 1
                l += 1
        
        return shortest if shortest is not None else ""


        

