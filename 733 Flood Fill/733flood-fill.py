class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if color == original:
            return image
        row, col = len(image), len(image[0])
        def dfs(r, c):
            if r <0 or r >= row or c < 0 or c >= col:
                return 
            if image[r][c] ==  color or image[r][c] != original:
                return
            
                
            image[r][c] = color
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        dfs(sr, sc)
        return image
