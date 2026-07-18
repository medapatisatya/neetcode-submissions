class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) * len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            r,c = mid // len(matrix[0]), mid % len(matrix[0])

            if target == matrix[r][c]: return True
            elif target > matrix[r][c]: low = mid + 1
            else: high = mid - 1
        
        return False