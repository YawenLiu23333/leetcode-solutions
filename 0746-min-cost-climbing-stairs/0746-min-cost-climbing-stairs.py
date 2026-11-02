class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(cost):
                return 0 # not sure what to return here but cost == len is 0

            memo[i] = cost[i] + min(dfs(i +1), dfs(i+2))

            return memo[i]

        return min(dfs(0), dfs(1))