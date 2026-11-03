
class Solution:
    def rob(self, nums: list[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0

            # Option 1: take nums[i]
            take = nums[i] + dfs(i + 2)

            # Option 2: skip nums[i]
            skip = dfs(i + 1)

            return max(take, skip)

        return dfs(0)
