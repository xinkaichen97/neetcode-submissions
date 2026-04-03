class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag, negDiag = set(), set()
        grid = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in grid]
                res.append(copy)
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                grid[r][c] = "Q"
                
                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                grid[r][c] = "."

        backtrack(0)
        return res