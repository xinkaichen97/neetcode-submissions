class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minH = maxH = grid[0][0]
        for row in grid:
            minH = min(minH, min(row))
            maxH = max(maxH, max(row))

        visit = set()
        def dfs(node, t):
            r, c = node
            if r < 0 or c < 0 or r >= n or c >= n or (r, c) in visit or grid[r][c] > t:
                return False
            if r == n - 1 and c == n - 1:
                return True
            visit.add((r, c))
            return dfs((r + 1, c), t) or dfs((r - 1, c), t) or dfs((r, c + 1), t) or dfs((r, c - 1), t)
            
        l, r = minH, maxH
        while l < r:
            m = (l + r) // 2
            if dfs((0, 0), m):
                r = m
            else:
                l = m + 1
            visit = set()
        return r
