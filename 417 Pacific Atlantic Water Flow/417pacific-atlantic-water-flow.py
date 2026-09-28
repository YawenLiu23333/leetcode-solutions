class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        row, col = len(heights), len(heights[0])
        def dfs(r, c, visited):
            if (r, c) in visited:
                return 

            visited.add((r, c))

            for nr, nc in [[r +1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if 0 <= nr < row and 0 <= nc < col and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc, visited)

        pacific, atlantic = set(), set()
        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                if c == col -1 or r == row -1:
                    atlantic.add((r,c))
        pac_visited, atl_visited = set(), set()
        
        for r, c in pacific:
            dfs(r, c, pac_visited)
        for r, c in atlantic:
            dfs(r, c, atl_visited)

        res = list(pac_visited & atl_visited)

        return res

        

