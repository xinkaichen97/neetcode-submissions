class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1
        for num in nums:
            tmp = curMax * num
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(num, tmp, num * curMin)
            res = max(res, curMax)
        return res