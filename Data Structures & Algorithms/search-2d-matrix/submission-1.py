class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, h = 0, r*c-1

        while l <= h:
            m = (l+h)//2
            mr, mc = m//c, m%c
            if matrix[mr][mc] == target: return True
            elif matrix[mr][mc] < target: l = m + 1
            else: h = m - 1
        return False