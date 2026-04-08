class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            seen = set()
            for num in board[i]:
                if num != "." :
                    if num in seen:
                        return False
                    seen.add(num)

        for i in range(9):
            seen = set()
            for j in range(9):
                num = board[j][i]
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)

        for n in range(0, 9, 3):
            for m in range(0, 9, 3):
                seen = set()
                for i in range(n, n + 3):
                    for j in range(m, m + 3):
                        num = board[i][j]
                        if num != ".":
                            if num in seen:
                                return False
                            seen.add(num)

        return True

