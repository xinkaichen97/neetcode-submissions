class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count != 0:
                    q.append((count, time + n))
            else:
                time = q[0][1]
            if q and time == q[0][1]:
                heapq.heappush(heap, q.popleft()[0])
            
        return time