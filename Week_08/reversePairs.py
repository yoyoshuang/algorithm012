# 翻转对
# https://leetcode-cn.com/problems/reverse-pairs/
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = self.mergesort(nums, 0, n-1)
        return count
    
    def mergesort(self, nums, start, end):
        if end <= start:
            return 0
        mid = (start+end)>>1
        left = self.mergesort(nums, start, mid)
        right = self.mergesort(nums, mid+1, end)
        find = self.merge(nums, start, mid, end)
        return left+right+find
     
    def merge(self, nums, start, mid, end):
        tmp = []
        i, j = start, mid+1
        res = 0
        while i<=mid and j<=end:
            if nums[i]/2 > nums[j]:
                res += (mid-i)+1
                j += 1
            else:
                i += 1
        # 开始归并
        i, j = start, mid+1
        while i<=mid and j<=end:
            if nums[i]<nums[j]:
                tmp.append(nums[i])
                i+=1
            else:
                tmp.append(nums[j])
                j+=1
        while i<=mid:
            tmp.append(nums[i])
            i+=1
        while j <= end:
            tmp.append(nums[j])
            j+=1
        nums[start:end+1] = tmp
        return res 