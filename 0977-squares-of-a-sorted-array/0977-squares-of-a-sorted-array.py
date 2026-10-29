class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        heap = [abs(n) for n in nums]
        heapq.heapify(heap)
        print(heap)
        res = []
        while heap:
            temp = heapq.heappop(heap)
            res.append(temp * temp)
        return res
