class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Map a -> list of [b, a / b]
        adj = collections.defaultdict(list)  

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q, visit = deque([(src, 1)]), set()
            visit.add(src)

            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for nb, weight in adj[node]:
                    if nb not in visit:
                        q.append((nb, w * weight))
                        visit.add(nb)
            return -1

        return [bfs(q[0], q[1]) for q in queries]
        