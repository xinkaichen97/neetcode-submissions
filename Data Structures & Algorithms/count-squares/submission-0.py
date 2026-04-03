class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        qx, qy = point
        for x, y in self.points:
            if abs(x - qx) == abs(y - qy) and x != qx and y != qy:
                res += self.counts[(x, qy)] * self.counts[(qx, y)]
        return res
