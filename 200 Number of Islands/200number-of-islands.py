class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        island = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    queue = deque([(r,c)])
                    while queue:
                        cr, cc = queue.popleft()
                        for nr, nc in ((cr + 1, cc), (cr -1 , cc), (cr, cc + 1), (cr, cc -1)):
                            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                queue.append((nr, nc))
                    island += 1
        return island


