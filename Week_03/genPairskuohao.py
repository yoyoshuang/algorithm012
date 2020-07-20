# 生成括号
# 

def generateParenthesis(n):
    outs = []
    def gen(left, right, n,  s):
        # print(left, right)
        if (left== n and right == n):
            outs.append(s)
            return 
        
        if (left < n):
            gen(left+1, right, n, s+'(')
        if (right<left): 
            gen(left, right+1, n, s+')')   
    gen(0, 0, n, '')
    
    return outs
if __name__ == "__main__":
    n = 3
    print(generateParenthesis(n))
        

    
