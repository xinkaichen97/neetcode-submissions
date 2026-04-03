class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # helper function to see if Koko can finish at k
        def canFinish(k: int) -> bool:
            t = 0
            for p in piles:
                # if p is not divisible by k, add one (math.ceil)
                t += p // k
                if p % k:
                    t += 1
                if t > h:
                    return False
            return True

        # binary search from 1 to the max pile
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            # if can finish, search in the left and update answer
            if canFinish(mid):
                res = mid
                r = mid - 1
            # otherwise search in the right
            else:
                l = mid + 1
                
        return res