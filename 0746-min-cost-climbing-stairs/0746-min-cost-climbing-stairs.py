class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        @cache
        def dfs(i):
            if i >= len(cost):
                return 0

            take = cost[i] + dfs(i + 1)
            skip = cost[i] + dfs(i + 2)

            return min(take, skip)

        return min(dfs(0), dfs(1))
            