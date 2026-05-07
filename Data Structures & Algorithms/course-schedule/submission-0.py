class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)
            # For each pair [a, b] meaning "to take a, you must first take b", 
            # this builds an edge a → b. So g[a] is the list of courses that a depends on.

        # g = [[] for _ in range(numCourses)]
        # for a, b in prerequisites:
        #     g[a].append(b)

        # g = {}
        # for a, b in prerequisites:
        #     if a not in g:
        #         g[a] = []
        #     g[a].append(b)
        
        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses
        
        def dfs(node):
            state = states[node]
            if state == visited: return True
            elif state == visiting: return False
            
            states[node] = visiting

            for nei in g[node]:
                if not dfs(nei): 
                    return False
            
            states[node] = visited
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True