# 全排列2
# https://leetcode-cn.com/problems/permutations-ii/
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        outs = []
        n = len(nums)
        
        def dfs(pre, n, outs):
            if len(pre) == n:
                ls = [nums[k] for k in pre]
                if ls not in outs:
                    outs.append(ls)
                return 
            
            for i, num in enumerate(nums):
                if i not in pre :
                    pre.append(i)
                    # inds.append(i)
                    dfs(pre, n, outs)
                    pre.pop()
                    
        
        dfs([], n, outs)
        return outs