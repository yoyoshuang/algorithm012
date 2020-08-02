# 33. 搜索旋转排序数组
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        N = len(nums)
        left = 0 
        right = N-1
        # mid = (left+right)//2

        while left<=right:
            mid = (left +right)//2
         
            if nums[mid]==target:
                return mid
            if nums[0]<= nums[mid]: # 左边有序
                if nums[0]<=target<nums[mid]:
                    right = mid-1
                else:
                    left = mid+1

            else : # 右边有序
                if nums[mid]< target<=nums[N-1]:
                    left = mid+1
                else:
                    right = mid-1

        return -1