class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)*len(matrix[0]) - 1
        while l <= r:
            mid = ((l + r) // 2)
            row_mid = mid // len(matrix[0])
            col_mid = mid % len(matrix[0]) 
            if matrix[row_mid][col_mid] < target:
                l = mid + 1
            elif matrix[row_mid][col_mid] > target:
                r = mid - 1
            else:
                return True
        return False