class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_rows, n_cols = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, n_rows):
            for c in range(1, n_cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(n_rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(n_cols):
                matrix[0][c] = 0         
                