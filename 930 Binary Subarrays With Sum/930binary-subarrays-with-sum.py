class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        windows = {0:1}
        res = 0
        prefix = 0
        for n in nums:
            prefix += n
            diff = prefix - goal
            if diff in windows:
                res += windows[diff]
            windows[prefix] = 1 + windows.get(prefix, 0) 
        return res