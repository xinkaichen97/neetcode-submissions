class Solution:
    def reorganizeString(self, s: str) -> str:
        # create counts and max heap
        counts = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(maxHeap)

        # prev cannot be reused
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            
            # push back to heap
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # set prev to current
            if cnt != 0:
                prev = [cnt, char]

        return res
