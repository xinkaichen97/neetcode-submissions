class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        
        for i in range(n):
            nextdp = defaultdict(int)
            for total, count in dp.items():
                nextdp[total + nums[i]] += count
                nextdp[total - nums[i]] += count
            dp = nextdp

        return dp[target]