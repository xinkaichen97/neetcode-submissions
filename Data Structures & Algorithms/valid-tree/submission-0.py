class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        mapping = defaultdict(list)
        for src, dst in edges:
            mapping[src].append(dst)
            mapping[dst].append(src)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return False
                
            visit.add(node)
            for nb in mapping[node]:
                if nb == prev:
                    continue
                if not dfs(nb, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False

        return len(visit) == n
