class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        heap = [(grid[0][0], 0, 0)]
        visit = set()
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    maxT = max(t, grid[nr][nc])
                    heapq.heappush(heap, (maxT, nr, nc))

