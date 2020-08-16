# 363. 矩形区域不超过 K 的最大数值和
# https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        def dpmax(nums, k):
            res = -1*float('inf')
            pre = nums[0]
            for i in range(len(nums)):
                sum_ = 0
                for j in range(i, len(nums)):
                    sum_+=nums[j]
                    if sum_ > res and sum_ <=k:
                        res = sum_
            return res

            
        row = len(matrix)
        col = len(matrix[0])
        maxres = -1*float('inf')
        for left in range(col):
            rowsum = [0]*row
            for right in range(left, col):
                for i in range(row):
                    rowsum[i] += matrix[i][right]
                this_max = dpmax(rowsum, k)
                maxres = max(maxres, this_max)
        
        return maxres