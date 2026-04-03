class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix.reverse()
        # for i in range(n // 2):
        #     matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # for row in matrix:
        #     row.reverse()
        