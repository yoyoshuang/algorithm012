# 773. 滑动谜题
# https://leetcode-cn.com/problems/sliding-puzzle/
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = { 0: [1,3], 1: [0,2,4], 2: [1,5], \
                  3: [0,4], 4:[1,3,5], 5:[2,4]
                }
        board = board[0]+board[1]
        s = ''.join([str(c) for c in board])
        if s=='123450':
            return 0
        q = [(s, 0)]
        visited = {s}
        
        while q:
            cur, step = q.pop(0)
            zero_ind = cur.index('0')

            for move_ind in moves[zero_ind]:
                new_s = list(cur)
                new_s[move_ind], new_s[zero_ind] = new_s[zero_ind], new_s[move_ind]
                new_s = ''.join(new_s)
                if new_s == '123450':
                    return step+1
                if new_s not in visited:
                    q.append((new_s, step+1))
                    visited.add(new_s)
        return -1