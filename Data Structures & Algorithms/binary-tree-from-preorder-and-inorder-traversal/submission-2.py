# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        mp = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            nonlocal pre_idx
            node = TreeNode(preorder[pre_idx])
            pre_idx += 1
            mid = mp[node.val]

            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)
            return node
        
        return dfs(0, len(inorder) - 1)
        