class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        l, r = 0, num_rows * num_cols - 1
        while l <= r:
            mid = ((l + r) // 2)
            row_mid = mid // num_cols
            col_mid = mid % num_cols
            if matrix[row_mid][col_mid] < target:
                l = mid + 1
            elif matrix[row_mid][col_mid] > target:
                r = mid - 1
            else:
                return True
        return False