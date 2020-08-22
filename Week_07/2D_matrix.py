# 1091. 二进制矩阵中的最短路径
# https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1]==1:
            return -1
        if n<=2:
            return n
        q = [(0, 0, 1)]
        
        grid[0][0] = 1
        
        while(q):
            i, j, step = q.pop(0)
            
            for di, dj in [(-1,-1),(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1)]:
                next_i, next_j = i+di, j+dj
                if next_i == n-1 and next_j==n-1:
                    return step+1
                if 0<=next_i<n and 0<=next_j<n and grid[next_i][next_j]==0:
                    q.append((next_i, next_j, step+1))
                    grid[next_i][next_j] = 1
     
        return -1