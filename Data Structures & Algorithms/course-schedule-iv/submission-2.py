class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        isPrereq = [set() for _ in range(numCourses)]

        # build adjacency list and indegree array
        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegree[crs] += 1

        # Kahn's algorithm
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for nb in adj[node]:
                isPrereq[nb].add(node)
                isPrereq[nb].update(isPrereq[node])
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)

        return [u in isPrereq[v] for u, v in queries]
