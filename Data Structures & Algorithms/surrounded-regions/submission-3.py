class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True

    def connected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dsu = DSU(m * n + 1)

        for r in range(m):
            for c in range(n):
                if board[r][c] != "O":
                    continue
                if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                    dsu.union(m * n, r * n + c)
                else:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if board[nr][nc] == "O":
                            dsu.union(r * n + c, nr * n + nc)

        for r in range(m):
            for c in range(n):
                if not dsu.connected(m * n, r * n + c):
                    board[r][c] = "X"
                