# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
# 153. 寻找旋转排序数组中的最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:

        N = len(nums)
        if N <2:
            return nums[0]
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r) //2 
            if nums[0] < nums[mid]<nums[N-1]:
                return nums[0]
            if nums[mid]> nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[0] < nums[mid]:
                l = mid+1
            elif nums[mid]<nums[N-1]:
                r = mid-1
        
                
