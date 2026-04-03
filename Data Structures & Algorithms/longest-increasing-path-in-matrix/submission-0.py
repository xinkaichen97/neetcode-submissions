class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j, prev):
            if 0 <= i < m and 0 <= j < n and matrix[i][j] > prev:
                if (i, j) in memo:
                    return memo[(i, j)]
                curr = matrix[i][j]
                res = 1 + max(dfs(i, j + 1, curr), dfs(i, j - 1, curr), dfs(i + 1, j, curr), dfs(i - 1, j, curr))
                memo[(i, j)] = res
                return res
            else:
                return 0
            
        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
        return max(memo.values())