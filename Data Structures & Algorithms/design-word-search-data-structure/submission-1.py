class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
        
    def search(self, word: str) -> bool:
        def dfs(i, cur): #(index_in_word, current_node) "starting from node cur, can the rest of the word (from index i onward) be matched?"
            # base case: walked through the whole word
            if i == len(word):
                return cur.end_of_word
            
            c = word[i]
            if c == ".":
                # try every child — succeed if ANY one matches
                for child in cur.children.values(): #values gives you knows, dont care which key it is
                    if dfs(i + 1, child): #cur becomes its child and i+1
                        return True #found it we are done
                return False #nothing found it
            else:
                # normal letter — only one path to try
                if c not in cur.children:
                    return False
                return dfs(i + 1, cur.children[c]) #the path exists. Step down to that child and recurse on the rest of the word
        
        return dfs(0, self.root)

class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode # a dict mapping a character to the next node. 
        self.end_of_word = False #a flag: True means "a complete inserted word ends right here."


        
