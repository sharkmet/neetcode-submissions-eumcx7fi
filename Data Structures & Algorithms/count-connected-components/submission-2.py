class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs method
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * n
        
        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

        # q/bfs version
        # parent = list(range(n))   # each node is its own root initially
        # size = [1] * n            # size of each component (used for union by size)
        
        # def find(x):
        #     # path compression: flatten the tree as we go
        #     while parent[x] != x:
        #         parent[x] = parent[parent[x]]
        #         x = parent[x]
        #     return x
        
        # def union(x, y):
        #     rootX, rootY = find(x), find(y)
        #     if rootX == rootY:
        #         return False   # already in same component, no merge happened
        #     # union by size: attach smaller tree under larger root
        #     if size[rootX] < size[rootY]:
        #         rootX, rootY = rootY, rootX
        #     parent[rootY] = rootX
        #     size[rootX] += size[rootY]
        #     return True
        
        #Union Find version
        # res = n
        # for a, b in edges:
        #     if union(a, b):
        #         res -= 1
        # return res