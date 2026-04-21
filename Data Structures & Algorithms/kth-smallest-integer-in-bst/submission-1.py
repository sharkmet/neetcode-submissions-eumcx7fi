# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        count = 0

        def in_order(node):
            nonlocal result, count
            if not node:
                return

            in_order(node.left)
            
            count += 1
            if count == k:
                result = node.val
                return
            
            in_order(node.right)

        
        in_order(root)
        return result