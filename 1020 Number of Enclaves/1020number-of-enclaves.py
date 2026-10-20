class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        land = sum(sum(row) for row in grid)

        for r in range(row):
            queue.append((r, 0))
            queue.append((r, col -1))
        for c in range(col):
            queue.append((0, c))
            queue.append((row -1, c))

        while queue:
            nr, nc = queue.popleft()
            if grid[nr][nc] == 0:
                continue
           
            grid[nr][nc] = 0
            land -= 1

            for cr, cc in ((nr + 1, nc), (nr -1, nc), (nr, nc + 1), (nr, nc -1)):
                if 0 <= cr < row and 0 <= cc < col:
                    if grid[cr][cc] == 0:
                        continue
                    else:
                        queue.append((cr, cc))
        return land
