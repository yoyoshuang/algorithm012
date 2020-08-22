# 37. 解数独
# https://leetcode-cn.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0 or len(board[0]) == 0:
            return
        self.solve(board)
    
    def solve(self, board):
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.': 
                    for c in range(1,10):
                        if self.is_valid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    def is_valid(self, board, row, col, num):
        for k in range(0,9):
            if board[row][k]!='.' and board[row][k]== num : return False
            if board[k][col]!='.' and board[k][col]== num : return False
            if board[(row//3)*3+k//3][(col//3)*3+k%3] == num: return False
        return True 


                        