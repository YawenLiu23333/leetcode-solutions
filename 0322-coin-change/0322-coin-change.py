class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def dfs(remaining):
            if remaining == 0:
                return 0

            best = float('inf')

            for c in coins:
                if remaining >= c:
                    take = 1 + dfs(remaining - c)
                    best = min(best, take)

            return best

        res = dfs(amount)
        return res if res != float('inf') else -1
