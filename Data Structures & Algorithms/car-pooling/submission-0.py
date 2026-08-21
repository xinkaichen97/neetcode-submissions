class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort by start location
        trips.sort(key=lambda t: t[1])

        # pair of [end, numPassengers]
        minHeap = []
        curPass = 0

        for numPass, start, end in trips:
            # pop all trips with end <= current start
            while minHeap and minHeap[0][0] <= start:
                curPass -= heapq.heappop(minHeap)[1]

            # add count
            curPass += numPass
            if curPass > capacity:
                return False

            # push to heap
            heapq.heappush(minHeap, [end, numPass])

        return True
