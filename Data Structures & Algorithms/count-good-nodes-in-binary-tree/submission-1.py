# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque([(root, root.val)])
        
        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            maxval = max(node.val, maxval)
            if node.left:
                q.append((node.left, maxval))
            if node.right:
                q.append((node.right, maxval))
            
        return res