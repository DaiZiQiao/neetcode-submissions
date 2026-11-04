class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col - 1

        while left <= right:
            mid = (left+right) // 2

            new_row = mid // col
            new_col = mid % col
            val = matrix[new_row][new_col]

            if val < target:
                left = mid + 1
            elif val > target:
                right = mid - 1
            else:
                return True
        return False