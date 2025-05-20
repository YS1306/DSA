class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n < 0):
            return self.myPow(1/x, -1*n)
        if n == 1:
            return x
        if n == 0:
            return 1
        if(n%2) == 1:
            return x*self.myPow(x,int(n/2))**2
        else:
            return self.myPow(x, int(n/2))**2