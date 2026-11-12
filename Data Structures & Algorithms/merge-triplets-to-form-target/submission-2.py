class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        a = b = c = False
        count = 0
        for a_i, b_i, c_i in triplets:
            if a_i > x or b_i > y or c_i > z:
                continue
            if a_i == x:
                a = True
            if b_i == y:
                b = True
            if c_i == z:
                c = True
        return a and b and c
        