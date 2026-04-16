class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix)
        n = len(matrix[0])
        r = m * n - 1

        while l <= r:
            middle = l + (r-l)//2
            idx_row = (middle // n)
            idx_col = middle % n

            if matrix[idx_row][idx_col] == target:
                return True
            elif matrix[idx_row][idx_col] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False
        