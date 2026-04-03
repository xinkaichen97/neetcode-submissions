class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
    
    def find(self, u):
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = self.parent[pu]
        else:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = self.parent[pv]
        return True


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        positions = sorted([(grid[r][c], r, c) for r in range(n) for c in range(n)])
        for t, r, c in positions:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
                    dsu.union(r * n + c, nr * n + nc)
            if dsu.find(0) == dsu.find(n * n - 1):
                return t



