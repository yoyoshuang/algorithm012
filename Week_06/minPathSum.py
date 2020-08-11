# 最小路径和
# https://leetcode-cn.com/problems/minimum-path-sum/submissions/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [ [0] * (n+1) ] * (m+1)

        for i in range(m-1, -1 , -1):
            for j in range(n-1, -1, -1):
                if j == n-1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                    continue
                if i == m-1: 
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                    continue
                else:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        # print(dp)
        return dp[0][0]
