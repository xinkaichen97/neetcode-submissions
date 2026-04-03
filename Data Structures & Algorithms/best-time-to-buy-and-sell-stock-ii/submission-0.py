class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def rec(i, bought):
            if i == len(prices):
                return 0
            if (i, bought) in memo:
                return memo[(i, bought)]
            res = rec(i + 1, bought)
            if bought:
                res = max(res, prices[i] + rec(i + 1, False))
            else:
                res = max(res, -prices[i] + rec(i + 1, True))
            memo[(i, bought)] = res
            return res

        return rec(0, False)