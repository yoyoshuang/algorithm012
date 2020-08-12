# 221. 最大正方形
# https://leetcode-cn.com/problems/maximal-square/
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 输入: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4

def max_square(matrix):
 
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    
    n = len(matrix)  # 行  
    m = len(matrix[0]) # 列
    # print(n, m)
    
    dp = [[0] * m for _ in range(n)] 
    max_num= 0
    for i in range(m):
        dp[0][i] = int(matrix[0][i])  
        max_num = max(max_num, dp[0][i])

    for j in range(n):
        dp[j][0] = int(matrix[j][0])
        max_num = max(max_num, dp[j][0])
 
    # max_num= 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
            else:
                dp[i][j] = 0
            if dp[i][j] >  max_num:
                max_num = dp[i][j]

    return max_num*max_num



if __name__ == "__main__":
    nums = [[1, 0, 1, 0, 0],
            [1, 0 ,1 ,1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]]
    nums = [["1","1","1","1","0"],
    ["1","1","1","1","0"],
    ["1","1","1","1","1"],
    ["1","1","1","1","1"],
    ["0","0","1","1","1"]]
print(max_square(nums))