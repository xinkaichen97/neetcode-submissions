class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for val in range(1, amount + 1):
            for coin in coins:
                if val >= coin:
                    dp[val] = min(dp[val], 1 + dp[val - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1