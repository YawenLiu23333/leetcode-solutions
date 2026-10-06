class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda point:point[1])
        res = 1
        preve = points[0][1]
        for start, end in points[1:]:
            if start > preve:
                preve = end
                res += 1
        return res
