# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n+1)
        dp[1] = 1
        dp[0] = 1
    
        s = '%'+s
        print(s)
        for i in range(2, n+1):
            if s[i] != '0':
                dp[i] = dp[i-1]
          
            if 10<=int(s[i-1:i+1]) <= 26 :
             
                dp[i] +=  dp[i-2]
            print(i, dp[i])
            
        return dp[n]


