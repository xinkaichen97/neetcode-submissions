class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            
            res = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j))
            
            memo[i] = res
            return res
        
        return max(dfs(i) for i in range(n))
        