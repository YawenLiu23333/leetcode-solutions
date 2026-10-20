class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        window = 0
        res = float('inf')
        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                res = min(r - l + 1, res)
                window -= nums[l]
                l += 1

        return res if res !=float('inf') else 0