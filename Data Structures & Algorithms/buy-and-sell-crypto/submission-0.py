class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        slow, fast = 0, 1
        while fast < len(prices):
            if prices[slow] < prices[fast]:
                ans = max(ans, prices[fast] - prices[slow])
            else:
                slow = fast
            fast += 1
        return ans