class Solution:
    def numSquares(self, n: int) -> int:
        # top-down DP
        memo = {}

        def dfs(target):
            if target == 0:
                return 0
            if target in memo:
                return memo[target]

            res = target
            # try largest squares first
            max_i = int(target ** 0.5)
            for i in range(max_i, 0, -1):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i * i))

            memo[target] = res
            return res

        return dfs(n)
