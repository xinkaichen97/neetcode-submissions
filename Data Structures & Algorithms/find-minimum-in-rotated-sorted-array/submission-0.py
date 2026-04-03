class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[r] >= nums[l]:
                res = min(res, nums[l])
                return res
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            res = min(res, nums[m])
        return res