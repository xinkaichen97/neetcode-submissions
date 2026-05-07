class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canFinish(cap):
            d, curr = 1, 0
            for w in weights:
                if curr + w > cap:
                    d += 1
                    curr = 0
                curr += w
            return d <= days

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            cap = (l + r) // 2
            if canFinish(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
                
        return res
