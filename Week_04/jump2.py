# 跳跃游戏2
# https://leetcode-cn.com/problems/jump-game-ii/submissions/
class Solution:
    
    def jump(self, nums: List[int]) -> int:
        
        self.count = 0
        def bfs(nums, i, count):
            n = len(nums)
            if i >= n-1:
                return
            self.count += 1
            maxnow = 0
            if nums[i]+i >=n-1: return
            for k in range(i+1, nums[i]+i+1):
                if nums[k]+k > maxnow:
                    j = k
                    maxnow = nums[k]+k
            bfs(nums, j, count)

        bfs(nums,0, self.count)
        return self.count
