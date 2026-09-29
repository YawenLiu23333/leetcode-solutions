class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        def dfs(i, total, cur):
            if total > n or len(cur) > k:
                return

            if total == n and len(cur) == k:
                res.append(cur.copy())
                return

            for j in range(i + 1, 10):
                cur.append(j)
                dfs(j, total + j, cur)
                cur.pop()
        
        dfs(0, 0, [])
        return res
