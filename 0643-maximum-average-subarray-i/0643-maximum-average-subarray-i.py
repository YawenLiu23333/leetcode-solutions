class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = 0
        res = float('-inf')
        
        l = 0
        for r in range(len(nums)):
            window += nums[r]
            if r - l + 1 > k:
                window -= nums[l]
                l += 1
            if r - l + 1 == k:
                res = max(res, window)
        return res/k