class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(len(board))]
        col_sets = [set() for _ in range(len(board))]
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board)):
                num = board[r][c]
                if num == ".":
                    continue
                if num in row_sets[r]:
                    return False
                if num in col_sets[c]:
                    return False
                if num in subgrid_sets[r//3][c//3]:
                    return False
                
                row_sets[r].add(num)
                col_sets[c].add(num)
                subgrid_sets[r//3][c//3].add(num)
        return True