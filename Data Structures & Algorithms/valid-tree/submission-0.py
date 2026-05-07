class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree on n nodes has two defining properties:
        # Connected — every node reachable from every other
        # Acyclic — no cycles
        if len(edges) != n - 1:
            return False
        
        #create a 2d list of each nodes neighbors
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in g[node]:
                #undirected so needed or else it looks lika cycle
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        #explicitly checking if it is connected by not nessary
        return dfs(0, -1) and len(visited) == n