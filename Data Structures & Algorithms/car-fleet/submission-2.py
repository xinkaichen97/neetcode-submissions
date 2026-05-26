class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        res = 0
        pairs = [(p, s) for p, s in sorted(zip(position, speed), reverse=True)]

        prev = 0
        for p, s in pairs:
            curr = (target - p) / s
            if curr > prev:
                res += 1
                prev = curr
        
        return res