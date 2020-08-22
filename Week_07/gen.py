# 基因变化
# https://leetcode-cn.com/problems/minimum-genetic-mutation/submissions/
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        front = {start}
        back = {end}
        res = 0
        while front:
            res += 1
            next_front = set()
            for gen in front:
                for i in range(len(gen)):
                    for c in ['A','C','G','T']:
                        if c != gen[i]:
                            new_gen = gen[:i]+c+gen[i+1:]
                            if new_gen in back:
                                return res
                            if new_gen in bank:
                                bank.remove(new_gen)
                                next_front.add(new_gen)
            front = next_front
            if len(front)> len(next_front):
                front, back = back, front
        
        return -1
