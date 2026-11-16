class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        heap = [(-v, n) for n, v in count.items()]
        heapq.heapify(heap)

        res = []
        while k > 0:
            freq, temp = heapq.heappop(heap)
            res.append(temp)
            k -= 1

        return res