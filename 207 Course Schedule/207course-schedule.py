class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre = defaultdict(list)
        for a, b in prerequisites:
            pre[a].append(b)

        status = {}

        def dfs(c):
            if c in status and status[c] == 'safe':
                return True

            if c in status and status[c] == 'visiting':
                return False

            status[c] = 'visiting'

            for nei in pre[c]:
                if not dfs(nei):
                    return False

            status[c] = 'safe'
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

