class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs():
            q = deque()
            for r in range(m):
                for c in range(n):
                    if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == "O":
                        board[r][c] = "#"
                        q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                        board[nr][nc] = "#"
                        q.append((nr, nc))

        bfs()
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
                
                
