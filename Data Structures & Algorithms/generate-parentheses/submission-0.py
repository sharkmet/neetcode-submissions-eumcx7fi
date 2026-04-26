class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res = []

        # def backtrack(sol, open_count, close_count):
        #     if len(sol) == 2 * n:
        #         res.append(sol)
        #         return
            
        #     if open_count < n:
        #         backtrack(sol + "(", open_count + 1, close_count)
        #     if close_count < open_count:
        #         backtrack(sol + ")", open_count, close_count + 1)
        
        # backtrack("", 0, 0)
        # return res

        res, sol = [], ""
        open = 0
        close = 0

        def backtrack():
            nonlocal open
            nonlocal close
            nonlocal sol  # need this since we reassign sol

            if len(sol) == 2*n:
                res.append(sol)
                return
            
            if open < n:
                sol += "("
                open += 1
                backtrack()
                sol = sol[:-1]   # undo
                open -= 1

            if close < open:
                sol += ")"
                close += 1
                backtrack()
                sol = sol[:-1]   # undo
                close -= 1

        backtrack()
        return res


