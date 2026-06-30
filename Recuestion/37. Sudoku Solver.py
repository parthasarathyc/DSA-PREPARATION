from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(r, c, ch):
            # check row
            for i in range(9):
                if board[r][i] == ch:
                    return False
            # check column
            for i in range(9):
                if board[i][c] == ch:
                    return False
            # check 3x3 box
            boxRow, boxCol = 3 * (r // 3), 3 * (c // 3)
            for i in range(boxRow, boxRow + 3):
                for j in range(boxCol, boxCol + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in map(str, range(1, 10)):
                            if isValid(r, c, ch):
                                board[r][c] = ch
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True

        backtrack()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
sol.solveSudoku(board)
for row in board:
    print(row)
