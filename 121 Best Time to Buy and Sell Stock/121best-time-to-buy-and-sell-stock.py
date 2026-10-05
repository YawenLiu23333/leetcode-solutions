class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cur_min = float('inf')
        res = 0
        for p in prices:
            res = max(res, p - cur_min)
            cur_min = min(p, cur_min)

        return res
