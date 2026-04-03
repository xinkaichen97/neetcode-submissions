class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        for crs, pre in prerequisites:
            mapping[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if mapping[crs] == []:
                return True
            
            visit.add(crs)
            for pre in mapping[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            mapping[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

            
