class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        diff = total - x
        if diff == 0:
            return len(nums)
        if diff < 0:
            return -1

        l = 0
        cur = 0
        max_len = 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur > diff:
                cur -= nums[l]
                l += 1
            if cur == diff:
                max_len= max(max_len, r - l + 1)
        if max_len == 0:
            return -1
        return len(nums) - max_len
            
