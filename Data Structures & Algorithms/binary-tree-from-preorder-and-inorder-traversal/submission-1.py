# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        indices = {val:idx for idx, val in enumerate(inorder)}
        root_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            nonlocal root_idx
            root_val = preorder[root_idx]
            root_idx += 1

            root = TreeNode(root_val)
            mid = indices[root_val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        
        return dfs(0, len(inorder) -  1)
        