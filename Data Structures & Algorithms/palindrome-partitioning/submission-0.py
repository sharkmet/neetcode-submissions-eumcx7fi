class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res, sol = [], []

        def is_palindrome(t):
            return t == t[::-1]

        def backtrack(start, i):
            if start == len(s):
                res.append(sol[:])
                return
            if i == len(s):
                return
            
            # decision 1: don't cut here, extend the current piece
            backtrack(start, i + 1)
            
            # decision 2: cut after i, if s[start:i+1] is a palindrome
            piece = s[start:i + 1]
            if is_palindrome(piece):
                sol.append(piece)
                backtrack(i + 1, i + 1)
                sol.pop()
        
        backtrack(0, 0)
        return res
