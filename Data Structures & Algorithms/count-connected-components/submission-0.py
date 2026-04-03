class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node):
            for nb in adj[node]:
                if nb not in visit:
                    visit.add(nb)
                    dfs(nb)
        res = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1
        return res

