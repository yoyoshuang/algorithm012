# 岛屿问题
# https://leetcode-cn.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i,j, grid, m, n): 
            grid[i][j] = 0
            for x, y in [(i-1, j),(i+1,j), (i, j-1), (i, j+1)]:
                if x>=0 and x<=n-1 and y>=0 and y<=m-1 and grid[x][y]=='1':
                    dfs(x, y, grid, m, n) 

        n = len(grid)
        if n==0:
            return 0
        m = len(grid[0])
        count = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] =='1':
                    count += 1
                    dfs(i,j,grid, m, n)
           
        return count