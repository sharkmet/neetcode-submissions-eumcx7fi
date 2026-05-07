class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        border_O = []

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] in ['#', 'X']:
                return
            elif board[r][c] == 'O':
                board[r][c] = '#'

            for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                dfs(r+i_off, c+j_off)

        # Duplicates on the corners are fine
        for j in range(n):
            border_O.append((0, j))
            border_O.append((m-1, j))
        for i in range(m):
            border_O.append((i, 0))
            border_O.append((i, n-1))

        for r, c in border_O:
            dfs(r, c)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

        

