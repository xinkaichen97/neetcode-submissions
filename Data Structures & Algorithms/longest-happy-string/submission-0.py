class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""

        # create a max heap
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            # get the most frequent char
            count, char = heapq.heappop(maxHeap)
            # check if there are already two consecutive chars
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                # pop the next one
                nxt_cnt, nxt_char = heapq.heappop(maxHeap)
                res += nxt_char
                nxt_cnt += 1
                if nxt_cnt:
                    heapq.heappush(maxHeap, (nxt_cnt, nxt_char))
                # push the original one back
                heapq.heappush(maxHeap, (count, char))
            else:
                res += char
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))

        return res
