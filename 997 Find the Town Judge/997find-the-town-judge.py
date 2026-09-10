class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming, outgoing = [0] * (n + 1), [0] * (n + 1)
        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1
        
        for p in range(1, n + 1):
            if outgoing[p] == 0 and incoming[p] == n - 1:
                return p
        
        return -1
        