class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        seen = set()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    seen.add((i,j))

        distance = 0

        while q:
            q_size = len(q)
            distance += 1
            for _ in range(q_size):
                i, j = q.popleft()
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != -1 and (r, c) not in seen :
                        grid[r][c] = distance
                        seen.add((r, c))
                        q.append((r, c))

        