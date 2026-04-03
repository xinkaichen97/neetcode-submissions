class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        counts = {}
        maxCount = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > maxCount:
                res = num
                maxCount = counts[num]
        return res
