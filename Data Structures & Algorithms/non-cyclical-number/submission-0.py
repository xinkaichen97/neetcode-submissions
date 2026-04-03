class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            n = self.getSum(n)
            if n in seen:
                return False
            seen.add(n)
        return True
    
    def getSum(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n = n // 10
        return res