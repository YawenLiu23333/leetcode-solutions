class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda interval:interval[0])
        res = 0
        temp = intervals[0]
        for start, end in intervals[1:]:
            if start < temp[1]:
                res += 1
                if end < temp[1]:
                    temp = [start, end]
            else:
                temp = [start, end]
        return res

