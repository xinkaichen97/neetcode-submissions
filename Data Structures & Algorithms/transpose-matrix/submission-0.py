class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n_row, n_col = len(matrix), len(matrix[0])
        res = [[0] * n_row for _ in range(n_col)]

        for r in range(n_row):
            for c in range(n_col):
                res[c][r] = matrix[r][c]

        return res
        