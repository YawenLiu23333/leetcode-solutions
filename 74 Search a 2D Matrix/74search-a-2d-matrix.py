class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col -1
        while l <= r:
            m = (l + r) //2
            ro = m // col
            co = m % col
            if matrix[ro][co] == target:
                return True
            elif matrix[ro][co] < target:
                l = m + 1
            else:
                r = m - 1
        return False
            


