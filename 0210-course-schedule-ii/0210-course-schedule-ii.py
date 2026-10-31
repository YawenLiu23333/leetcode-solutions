class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        pre = defaultdict(list)
        for a, b in prerequisites:
            pre[a].append(b)

        status = {}
        res = []

        def dfs(c):
            if c in status and status[c] == 'safe':
                return True
            if c in status and status[c]== 'visiting':
                return False

            status[c] = 'visiting'

            for nei in pre[c]:
                if not dfs(nei):
                    return False
            
            status[c] = 'safe'
            res.append(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

