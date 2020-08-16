# 编辑距离
# https://leetcode-cn.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n*m == 0:
            return n+m
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i + j == 0:
                    dp[i][j] = 0
                    continue
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = dp[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        return dp[n][m]

