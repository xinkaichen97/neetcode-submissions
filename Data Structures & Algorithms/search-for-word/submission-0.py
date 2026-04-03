class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_row, n_col = len(board), len(board[0])
        seen = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if min(r, c) < 0 or r >= n_row or c >= n_col or word[i] != board[r][c] or (r, c) in seen:
                return False
            
            seen.add((r, c))
            res = backtrack(r + 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c - 1, i + 1)
            seen.remove((r, c))
            return res

        for r in range(n_row):
            for c in range(n_col):
                if backtrack(r, c, 0):
                    return True
        
        return False