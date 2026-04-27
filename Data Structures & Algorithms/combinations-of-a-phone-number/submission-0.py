class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        n = len(digits)
        res, sol = [], ""
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(i):
            nonlocal sol
            if i == n:
                res.append(sol)
                return
            
            letters = digit_map[digits[i]]
            for l in letters:
                sol += l
                backtrack(i+1)
                sol = sol[:-1]

        backtrack(0)
        return res