class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return 0
            if rank[pu] > rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pu]
            return 1
        
        res = n
        for u, v in edges:
            res -= union(u, v)
        return res

