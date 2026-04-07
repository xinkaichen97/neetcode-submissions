class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        res = set()
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
            if counts[num] > len(nums) // 3:
                res.add(num)
        return list(res)