class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, cursum):
            if cursum == amount:
                return 1
            if i == len(coins) or cursum > amount:
                return 0
            if (i, cursum) in dp:
                return dp[(i, cursum)]

            dp[(i, cursum)] = dfs(i, cursum + coins[i]) + dfs(i + 1, cursum)
            return dp[(i, cursum)]
        
        return dfs(0, 0)
