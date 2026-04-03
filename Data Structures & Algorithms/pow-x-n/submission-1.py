class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            x, n = 1 / x, -n
    
        res = self.myPow(x * x, n // 2)
        
        return x * res if n % 2 else res