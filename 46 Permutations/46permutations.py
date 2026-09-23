class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) ==1:
            return [nums]
        res = []
        per = []
        def dfs(per):
            if len(per) == len(nums):
                res.append(per.copy())
                return

            for n in nums:
                if n in per:
                    continue
                per.append(n)
                dfs(per)
                per.pop()
        dfs(per)
        return res

