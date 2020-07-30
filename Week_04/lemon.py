# 柠檬水找零
# https://leetcode-cn.com/problems/lemonade-change/description/
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            
            if i==5:
                five += 1
             
            elif i == 10:
                five -= 1
                ten += 1
                if five < 0:
                    return False
            if i == 20:
                if five and ten:
                    five -= 1
                    ten -=1
                elif five>=3:
                    five -= 3
                else:
                    return False

        return True