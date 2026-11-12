class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval:interval[0])
        res = []
        cur = intervals[0]
        for start, end in intervals[1:]:
            if start <= cur[1]:
                cur = [cur[0], max(cur[1],end)]
            else:
                res.append(cur)
                cur = [start, end]
        res.append(cur)
        return res


