class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        ROWS, COLS = len(board), len(board[0])
        path = set() # temporarily overwrite board[r][c] = "#" before recursing and restore it after. Could work aswell

        def backtrack(row, col, i):
            if i == n:
                return True

            if (row < 0 or col < 0 or row >= ROWS or col >= COLS      # We return false if (row, col) is out of bounds 
                or word[i] != board[row][col] or (row, col) in path): # or if board[row][col] != word[i] or if it is the path already
                return False

            
            path.add((row, col))
            res = (backtrack(row + 1, col, i + 1) or
               backtrack(row - 1, col, i + 1) or
               backtrack(row, col + 1, i + 1) or
               backtrack(row, col - 1, i + 1))

            path.remove((row, col))   # backtrack
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False

        