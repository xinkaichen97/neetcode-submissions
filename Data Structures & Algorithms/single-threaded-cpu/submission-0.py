class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort by start time and duration
        tasks = sorted([(start, duration, i) for i, (start, duration) in enumerate(tasks)])
        currTime = 0
        heap = []
        res = []
        idx = 0

        # stop if heap is empty or no task remains
        while heap or idx < len(tasks):
            if not heap and tasks[idx][0] > currTime:
                currTime = tasks[idx][0]
            
            # add all tasks with start time before currTime
            while idx < len(tasks) and tasks[idx][0] <= currTime:
                start, duration, i = tasks[idx]
                heapq.heappush(heap, (duration, i))
                idx += 1
            
            # pop the task with the shortest duration
            if heap:
                duration, i = heapq.heappop(heap)
                currTime += duration
                res.append(i)
            
        return res
