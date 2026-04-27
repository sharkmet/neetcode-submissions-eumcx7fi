class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, pos_diag, neg_diag = set(), set(), set()
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # place
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # undo (backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
        