class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        mapping = {}

        def dfs(i, target):
            if i >= len(nums):
                return target == 0
            if target == 0:
                return True

            if (i, target) in mapping:
                return mapping[(i, target)]

            mapping[(i, target)] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            return mapping[(i, target)]
        
        return dfs(0, target)
