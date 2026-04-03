class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            nxt = r
            while l <= r:
                nxt = max(nxt, l + nums[l])
                l += 1
            l = r + 1
            r = nxt
            res += 1
        return res

