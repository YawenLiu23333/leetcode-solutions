class Solution:
    def rob(self, nums: list[int]) -> int:
        
        @cache
        def dfs(i, cur):
            if i >= len(nums):
                return 0

            take = nums[i] + dfs(i + 2, cur)
            leave = dfs(i + 1, cur)

            return max(take, leave)

        return dfs(0, 0)
