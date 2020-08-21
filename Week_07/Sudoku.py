# 36. 有效的数独
# https://leetcode-cn.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        block = [{} for _ in range(9)]

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num != '.':
                    num = int(num)

                    b_ind = i//3 *3 + j//3
                    row[i][num] = row[i].get(num, 0)+1
                    col[j][num] = col[j].get(num, 0)+1
                    block[b_ind][num] = block[b_ind].get(num,0) +1

                    if row[i][num]>1 or col[j][num]>1 or block[b_ind][num]>1:
                        return False
        return True




