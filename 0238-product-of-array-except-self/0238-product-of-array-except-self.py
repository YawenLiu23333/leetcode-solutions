class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        # calc prefix
        cur = 1
        for i, n in enumerate(nums):
            res[i] = cur
            cur *= n

        # calc postfix
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res

