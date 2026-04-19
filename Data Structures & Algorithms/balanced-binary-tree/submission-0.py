# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def height(node):
            nonlocal isBalanced

            if not node:
                return 0
            
            leftHeight = height(node.left)
            rightHeight = height(node.right)

            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False
            
            return 1 + max(leftHeight, rightHeight)
        
        height(root)
        return isBalanced

        
        