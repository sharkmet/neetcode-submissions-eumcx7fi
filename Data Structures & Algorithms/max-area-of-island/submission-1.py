class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >=n or grid[i][j] != 1:
                return 0
            else:
                grid[i][j] = 0
                return 1 + dfs(i, j+1) +dfs(i, j-1) +dfs(i+1, j) + dfs(i-1, j)
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area

    #     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # m, n = len(grid), len(grid[0])
    # visited = set()

    # def dfs(i, j):
    #     if (i < 0 or i >= m or j < 0 or j >= n
    #             or grid[i][j] != 1 or (i, j) in visited):
    #         return 0
    #     visited.add((i, j))
    #     return 1 + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j)

    # max_area = 0
    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] == 1 and (i, j) not in visited:
    #             max_area = max(max_area, dfs(i, j))
    # return max_area
        