# 全排列
# https://leetcode-cn.com/problems/permutations/submissions/
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outs = []
        n = len(nums)
        
        def dfs( pre, n, outs ):
            if len(pre)==n:
                outs.append(pre.copy())
                return
            
            for  num  in  nums:
                if num in pre:
                    continue
                pre.append(num)
                dfs(pre, n, outs)
                pre.pop()
        
        dfs([], n, outs)
        return outs