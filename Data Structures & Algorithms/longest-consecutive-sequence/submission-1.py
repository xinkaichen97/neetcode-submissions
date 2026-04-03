class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numset:
                curr = 1
                while num + 1 in numset:
                    num += 1
                    curr += 1
                res = max(res, curr)
        return res

            