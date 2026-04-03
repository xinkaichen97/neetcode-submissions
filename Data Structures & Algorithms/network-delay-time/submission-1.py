class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        visit = set()
        heap = [(0, k)]
        res = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node not in visit:
                visit.add(node)
                res = time
                for nb, w in adj[node]:
                    heapq.heappush(heap, (time + w, nb))
        return res if len(visit) == n else -1