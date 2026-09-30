class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        cur = {1:0, 0:0}
        #freqeunt lookup, O(1)
        res = float('-inf')
        l = 0
        for r in range(len(nums)):
            cur[nums[r]] += 1
            while cur[0] > k:
                cur[nums[l]] -= 1
                l += 1
            res = max(res, r -l + 1)
        return res
