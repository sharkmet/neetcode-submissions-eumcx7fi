class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        g = defaultdict(list)
        courses = prerequisites
        for a, b in courses:
            g[a].append(b)
            # For each pair [a, b] meaning "to take a, you must first take b", 
            # this builds an edge a → b. So g[a] is the list of courses that a depends on.
    
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses
        
        #True if no cycle, False if cycle
        def dfs(i):
            if states[i] == VISITING: return False
            elif states[i] == VISITED: return True
            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei): 
                    return False
            
            states[i] = VISITED
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order