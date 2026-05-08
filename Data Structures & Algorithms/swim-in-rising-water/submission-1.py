class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        # min-heap of (max_elevation_on_path_so_far, row, col)
        heap = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            t, r, c = heapq.heappop(heap)
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    # the cost to reach the neighbor is max(current path max, neighbor's elevation)
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))
