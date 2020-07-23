class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x
        
        if n < 0:
            return self.myPow(1/x, -n)
        
        even = self.myPow(x, n//2)
        odd = even * x
      
        if n % 2 ==1:
            return odd * even
        if n % 2 ==0:
            return even * even