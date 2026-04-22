# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs_sum(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left = dfs_sum(node.left)
            right = dfs_sum(node.right)

            # at THIS node, path can go left→node→right (the "bend")
            sum = node.val + max(left, 0) + max(right, 0)
            max_sum = max(max_sum, sum)

            # but returning up, parent can only extend through ONE side
            return node.val + max(left, right, 0)
        
        dfs_sum(root)
        return max_sum
        