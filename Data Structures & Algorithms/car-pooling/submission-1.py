class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # find the left and right most values (or just 0-1000)
        L, R = float("inf"), float("-inf")
        for _, start, end in trips:
            L = min(L, start)
            R = max(R, end)

        # find pass change for the array
        N = R - L + 1
        passChange = [0] * (N + 1)
        for numPass, start, end in trips:
            passChange[start - L] += numPass
            passChange[end - L] -= numPass

        # sweep through each change
        curPass = 0
        for change in passChange:
            curPass += change
            if curPass > capacity:
                return False

        return True
