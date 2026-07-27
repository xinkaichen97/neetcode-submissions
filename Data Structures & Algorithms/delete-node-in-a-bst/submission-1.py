# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        parent = None
        curr = root

        # Find the node to delete
        while curr and curr.val != key:
            parent = curr
            if key > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        if not curr:
            return root

        # Node with only one child or no child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not parent:
                return child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else:
            # Node with two children
            par = None  # parent of right subTree min node
            delNode = curr
            curr = curr.right
            while curr.left:
                par = curr
                curr = curr.left

            if par:  # if there was a left traversal
                par.left = curr.right
                curr.right = delNode.right

            curr.left = delNode.left

            if not parent:  # if we're deleting root
                return curr

            if parent.left == delNode:
                parent.left = curr
            else:
                parent.right = curr

        return root
