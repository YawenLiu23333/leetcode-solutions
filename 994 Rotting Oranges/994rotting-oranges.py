class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        row, col = len(grid), len(grid[0])
        time, fresh = 0, 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue and fresh > 0:
            print(queue)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c -1)):
                    if  0 <= i < row and 0 <= j < col:
                        if grid[i][j] == 1:
                            grid[i][j] = 2
                            fresh -= 1
                            queue.append((i, j))
            time += 1
        return time if fresh == 0 else -1

