class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        res = [[0] * len(mat[0]) for _ in range(len(mat))]
        queue = deque()
        row, col = len(mat), len(mat[0])
        
        for m in range(row):
            for n in range(col):
                if mat[m][n] == 0:
                    queue.append((m, n))
        
        distance = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in ((r + 1, c), (r -1, c), (r, c+1), (r, c-1)):
                    if 0 <= nr < row and 0 <= nc < col:
                        if mat[nr][nc] == 1:
                             mat[nr][nc] = 0
                             queue.append((nr, nc))
                             res[nr][nc] = distance
            distance += 1
        return res
            
