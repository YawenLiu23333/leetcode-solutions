class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def dfs(index, cur, total):
            if total > target:
                return

            if total == target:
                res.append(cur.copy())
                return 
            
            for j in range(index, len(candidates)):
                cur.append(candidates[j])
                dfs(j, cur, total + candidates[j])
                cur.pop()

        dfs(0, [], 0)
        return res

