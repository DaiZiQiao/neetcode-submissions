class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target >= matrix[mid][0]:
                top = mid + 1
            else:
                bottom = mid - 1
        
        left = 0
        right = len(matrix[bottom]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[bottom][mid]:
                left = mid + 1
            elif target < matrix[bottom][mid]:
                right = mid - 1
            elif target == matrix[bottom][mid]:
                return True
        
        return False
        