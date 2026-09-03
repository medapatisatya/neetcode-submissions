class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols, boxes = [0 for i in range(9)], [0 for i in range(9)], [0 for i in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.': continue
                num = int(board[r][c])
                if rows[r] >> num & 1 or cols[c] >> num & 1 or boxes[(r//3)*3+c//3] >> num & 1:
                    return False

                rows[r] = rows[r] | 1 << num
                cols[c] = cols[c] | 1 << num
                boxes[(r//3)*3 + c//3] = boxes[(r//3)*3 + c//3] | 1 << num
        return True 