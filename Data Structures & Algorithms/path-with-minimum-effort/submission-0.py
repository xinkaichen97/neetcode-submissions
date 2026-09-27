class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]  # [diff, row, col]
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue
            visit.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visit:
                    continue

                newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minHeap, [newDiff, nr, nc])

        return 0
