class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add(w)

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent.children.get(ch) #parent is the node before the dfs call, so check if there is valid path
            if not node:
                return  # prefix not in trie, prune

            if node.word:
                result.append(node.word)
                node.word = None  # don't add this word again
                #dont return yet because longer words are still finable

            board[r][c] = '#'  # mark visited
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, node)
            board[r][c] = ch  # restore

            # Optimization: prune dead branches from the trie
            if not node.children: #Has no children left so can be skipped next time dfs reaches this part, word would hae already been returned
                parent.children.pop(ch) #we only pop a node when both its word is None (already collected) and its children dict is empty.

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # full word at terminal nodes, else None

    def add(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word
        