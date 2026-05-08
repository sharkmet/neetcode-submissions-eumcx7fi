class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adjacency list: char -> set of chars that must come after, use a set to prevent duplicate entries
        adj = {c: set() for w in words for c in w}
        
        # build edges from adjacent word pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # prefix violation check: if w1 is longer and w2 is a prefix of w1, that's an inconsistency.
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            # find first differing char
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    # only first char subsequent chars tell nothing about the ordering
                    break
        
        # DFS-based topological sort
        # visited[c]: False = currently in DFS path (gray), True = fully processed (black)
        # absent from dict = unvisited (white)
        # unvisited, visiting, visited
        visited = {}
        result = []
        
        def dfs(c):
            if c in visited:
                return visited[c]   # True if safe (already processed), False if cycle
            visited[c] = False   # mark as "in current path"
            for nei in adj[c]:
                if not dfs(nei):
                    return False   # cycle detected downstream
            visited[c] = True    # done processing this node
            result.append(c) #end up appending neighbors/decendants first, so just reverse order at the end
            return True
        #Post-order says "I'm done when all my dependencies-on-me are done." 
        # That naturally produces a list where things-depended-on come last. Reverse it, and things-depended-on come first.
        
        for c in adj:
            if not dfs(c):
                return ""
        
        return "".join(result[::-1])