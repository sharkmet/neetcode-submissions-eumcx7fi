# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        # result = ""
        # for i in range(len(res)):
        #     result += lst[i]
        #     if i < len(lst) - 1:   # don't add delimiter after the last one
        #         result += ","
        # return result
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # vals = []
        # current = ""
        # for char in s:
        # if char == ",":
        #     vals.append(current)
        #     current = ""
        # else:
        #     current += char
        # vals.append(current)   # don't forget the last chunk
        vals = data.split(",")
        i = 0
        
        def dfs():
            nonlocal i
            if vals[i] == "N":
                i += 1
                return None
            
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()




