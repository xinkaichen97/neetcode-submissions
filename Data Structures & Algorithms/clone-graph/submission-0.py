"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}
        if not node:
            return None
        
        def dfs(node):
            if node in mapping:
                return mapping[node]
            
            copy = Node(node.val)
            mapping[node] = copy
            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy
        
        return dfs(node)