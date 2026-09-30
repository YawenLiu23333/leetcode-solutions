class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        row, col = len(mat), len(mat[0])
        print(row, col)
        res = [[0 for _ in range(col)] for _ in range(row)]
        queue = deque()
        distance = 1 # as in time in orange
        one = 0
        #when theres no 1 in mat return what, no restrictions on 1s in q
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r, c))
                elif mat[r][c] == 1:
                    one += 1
        print(queue, one)

        #why do i need while queue here as in orange? it only keeps getting more 
        while queue and one > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in ((r + 1, c),(r -1, c),(r, c + 1),(r, c -1)):
                    if 0 <= nr < row and 0<= nc < col:
                        if mat[nr][nc] == 1:
                            mat[nr][nc] = 0
                            one -= 1
                            queue.append((nr, nc))
                            res[nr][nc] = distance
                            print(distance)

            distance += 1

        return res
                        


        