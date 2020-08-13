# 32. 最长有效括号
# https://leetcode-cn.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlenth = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
            
                if len(stack) == 0:
                    stack.append(i)
                else:
                    lenth = i-stack[-1]
                    maxlenth = max(maxlenth, lenth)
        return maxlenth