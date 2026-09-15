class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = set()
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            if board[r][c] != word[i]:
                return False
            if(r, c) in visited:
                return False
            
            visited.add((r, c))
            
            found = (
            dfs(i + 1, r + 1, c)
            or dfs(i + 1, r - 1, c)
            or dfs(i + 1, r, c + 1)
            or dfs(i + 1, r, c - 1)
            )
            visited.remove((r, c))

            return found

        for r in range(row):
            for c in range(col):
                if dfs(0, r, c):
                    return True
        return False

