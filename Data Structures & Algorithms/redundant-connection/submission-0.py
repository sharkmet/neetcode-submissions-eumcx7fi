class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))   # nodes are 1-indexed, so size n+1, if parent[x] == x it means it is a root
        size = [1] * (n + 1)
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if size[rootX] < size[rootY]:
                rootX, rootY = rootY, rootX
            parent[rootY] = rootX
            size[rootX] += size[rootY]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]