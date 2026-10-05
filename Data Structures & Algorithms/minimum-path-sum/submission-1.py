class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nRow, nCol = len(grid), len(grid[0])
        dp = [[float("inf")] * (nCol + 1) for _ in range(nRow + 1)]
        dp[nRow - 1][nCol] = 0

        for r in range(nRow - 1, -1, -1):
            for c in range(nCol - 1, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]
        