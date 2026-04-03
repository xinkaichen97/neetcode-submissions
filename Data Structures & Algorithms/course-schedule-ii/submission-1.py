class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        res = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:  # Already fully processed
                return True
            
            cycle.add(crs)
            for nb in adj[crs]:
                if not dfs(nb):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)  # Always add when first completing a node
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res