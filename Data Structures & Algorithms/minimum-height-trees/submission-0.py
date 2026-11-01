class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_cnt = {}
        leaves = deque()
        for src, nbs in adj.items():
            edge_cnt[src] = len(nbs)
            if len(nbs) == 1:
                leaves.append(src)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nb in adj[node]:
                    edge_cnt[nb] -= 1
                    if edge_cnt[nb] == 1:
                        leaves.append(nb)
                        