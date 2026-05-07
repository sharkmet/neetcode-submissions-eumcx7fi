class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        m = len(beginWord)
        
        # build pattern -> list of words sharing that pattern
        # Avoid directly comparing words as that time complexity is too large
        # dict key is the patern, and all words that share that pattern are in its list
        # We indirectly find neighbors this way O(n^2m) vs O(nm^2) better as m almost always smaller
        # for each of n words, build m patterns, each costing m to slice
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(m):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        
        # BFS
        visited = {beginWord}
        queue = deque([(beginWord, 1)])   # (word, number of words in sequence so far)
        
        while queue:
            word, length = queue.popleft()
            # Since BFS guarenteed to be the shortest possible path
            if word == endWord:
                return length
            
            # generate all patterns for current word, visit neighbors
            for i in range(m):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))
        
        return 0