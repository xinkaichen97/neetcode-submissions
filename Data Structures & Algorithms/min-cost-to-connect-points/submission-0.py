class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        visit = set()
        heap = [(0, 0)]
        while len(visit) < len(points):
            cost, node = heapq.heappop(heap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for nbCost, nb in adj[node]:
                if nb not in visit:
                    heapq.heappush(heap, (nbCost, nb))
        
        return res
        