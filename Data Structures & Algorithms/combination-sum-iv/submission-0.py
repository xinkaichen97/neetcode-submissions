class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # sort the nums and create memoization
        nums.sort()
        memo = {0: 1}

        # top-down
        def dfs(total):
            if total in memo:
                return memo[total]

            res = 0
            for num in nums:
                if total < num:
                    break
                res += dfs(total - num)
            memo[total] = res
            return res

        return dfs(target)
