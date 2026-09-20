class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
            
        return True if fast == 1 else False
    
    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n = n // 10
        return res
        