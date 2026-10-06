class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur = 0
        res = 0
        prefix = {0:-1}
        for i, n in enumerate(nums):
            if n == 0:
                cur -= 1
            else:
                cur += 1
            if cur in prefix:
                res = max(res, i - prefix[cur])
            else:
                prefix[cur] = i
        return res
        


