class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        check = set(nums)
        res = 0
        for n in check:
            if n -1 not in check:
                length = 1
                while n + length in check:
                    length += 1
                res = max(res, length)
        return res

        