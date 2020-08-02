# 74. 搜索二维矩阵
# https://leetcode-cn.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for row in matrix:
            nums.extend(row)

        if len(nums)<1:
            return False
        l,r = 0, len(nums)-1

        while l <=r:
            mid = (l+r) // 2
            if nums[mid]==target:
                return True
            if nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return False