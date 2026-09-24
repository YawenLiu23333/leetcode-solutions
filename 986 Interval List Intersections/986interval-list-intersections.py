class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        ai, bi = 0, 0
        res = []
        while ai < len(firstList) and bi < len(secondList):
            start = max(firstList[ai][0], secondList[bi][0])
            end = min(firstList[ai][1], secondList[bi][1])
            if start <= end:
                res.append([start, end])
            #start > end means no intersection on ai bi, move on

            if firstList[ai][1] > secondList[bi][1]:
                bi += 1
            else:
                ai += 1
        #if ai or bi remianing then no intersections to be appended

        return res



