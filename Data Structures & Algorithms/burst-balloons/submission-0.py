class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
                
            res = 0
            for i in range(l, r + 1):
                curr = nums[l - 1] * nums[i] * nums[r + 1]
                curr += dfs(l, i - 1) + dfs(i + 1, r)
                res = max(res, curr)
            memo[(l, r)] = res
            return res

        return dfs(1, len(nums) - 2)
