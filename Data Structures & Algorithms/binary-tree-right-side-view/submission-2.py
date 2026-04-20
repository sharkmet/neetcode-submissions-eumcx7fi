# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append(root)
        result = []
    
        while q:
            node = q.pop()
            result.append(node.val)

            for _ in range(len(q)):
                n = q.popleft()
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        return result

        