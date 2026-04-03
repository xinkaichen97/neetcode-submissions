class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                res = max(res, h * (idx - i))
                start = i
            stack.append((start, height))
        
        for idx, height in stack:
            res = max(res, height * (len(heights) - idx))

        return res