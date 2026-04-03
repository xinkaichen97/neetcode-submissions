class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            mapping[pre].append(crs)  # pre → crs (natural direction)
            indegree[crs] += 1     # crs has incoming edge

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        completed = 0
        while q:
            node = q.popleft()
            completed += 1
            for nb in mapping[node]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        
        return completed == numCourses

            
