class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        res = 1
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse=True)

        prevTime = (target - cars[0][0]) / cars[0][1]
        for pos, sp in cars[1:]:
            time = (target - pos) / sp
            if time > prevTime:
                res += 1
                prevTime = time

        return res
