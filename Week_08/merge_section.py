# 56. 合并区间
# https://leetcode-cn.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals)<1:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            pre = merged[-1]
            now = intervals[i]
            if pre[-1] >= now[0]:
                merged[-1][-1] = max(now[1], pre[1])
            else:
                merged.append(now)
        return merged

        