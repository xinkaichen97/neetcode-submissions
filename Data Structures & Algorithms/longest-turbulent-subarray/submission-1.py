class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # initialize sign as -1
        n = len(arr)
        res = cnt = 0
        sign = -1

        # compare each adjacent pair 
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                cnt = cnt + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i + 1]:
                cnt = cnt + 1 if sign == 1 else 1
                sign = 0
            else:
                cnt = 0
                sign = -1

            res = max(res, cnt)

        # plus one for the element count
        return res + 1
        