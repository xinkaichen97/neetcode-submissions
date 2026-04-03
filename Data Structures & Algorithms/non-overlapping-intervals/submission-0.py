class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end times
        intervals.sort(key = lambda x: x[1])

        # keep track of the previous end
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            # if prev end is greater than start, there's an overlap
            # already sorted by end times so the current end must be greater, we remove the current interval
            if prevEnd > intervals[i][0]:
                res += 1
            # if no overlap, update the previous end with the current end
            else:
                prevEnd = intervals[i][1]

        return res