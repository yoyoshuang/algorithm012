# 分发饼干
# https://leetcode-cn.com/problems/assign-cookies/description/

def findContentChildren(g , s):
        
        g_new = sorted(g)
        s_new = sorted(s)
        
        child_num = 0
        i = 0 # 指向 s
        j = 0 # 指向 g 
        while i < len(s_new) and j < len(g_new):
            # print(i)
            if s_new[i]>= g_new[j]:
                child_num +=1
                j += 1
                i += 1
            else:
                i += 1
        return child_num


if __name__ == "__main__":
    g = [10,9,8,7]
    s = [5,6,7,8]
    g = [1,2,3]
    s = [3]
    print(findContentChildren(g, s))