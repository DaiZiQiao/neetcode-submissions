class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        sub_grid = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if num in row_set[r]:
                    return False
                if num in col_set[c]:
                    return False
                if num in sub_grid[r//3][c//3]:
                    return False
                
                row_set[r].add(num)
                col_set[c].add(num)
                sub_grid[r//3][c//3].add(num)
        return True