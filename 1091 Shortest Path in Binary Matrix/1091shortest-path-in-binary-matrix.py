class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        queue = deque([(0, 0)])
        path = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n -1:
                    return path
                for nr, nc in ((r + 1,c + 1), (r + 1, c - 1), (r -1, c -1), (r -1, c + 1), (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < n and 0 <= nc < n:
                        
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 1
                            queue.append((nr, nc))
            path += 1
        
        return -1




       