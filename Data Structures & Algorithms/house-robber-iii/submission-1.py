# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # memoization
        memo = {None: 0}

        def dfs(root):
            if root in memo:
                return memo[root]

            memo[root] = root.val
            if root.left:
                memo[root] += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                memo[root] += dfs(root.right.left) + dfs(root.right.right)

            memo[root] = max(memo[root], dfs(root.left) + dfs(root.right))
            return memo[root]

        return dfs(root)
