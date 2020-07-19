# 66. 加一
# https://leetcode-cn.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lenth = len(digits)
        num = 0
        k = 0
        for i in range(lenth-1, -1, -1):
            num += digits[i]*10**k
            k += 1
        num += 1
        str_num = str(num)
        return [int(s) for s in str_num]