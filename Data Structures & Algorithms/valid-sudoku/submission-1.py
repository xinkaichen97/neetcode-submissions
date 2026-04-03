class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, square = set(), set(), set()

        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
        
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col:
                    return False
                col.add(board[i][j])
        
        for s in range(9):
            square = set()
            for i in range(3):
                for j in range(3):
                    r = (s // 3) * 3 + i
                    c = (s % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in square:
                        return False
                    square.add(board[r][c])
        
        return True