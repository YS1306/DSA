class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag = False
        for i in range(n):
            po = 2**i
            if n%po != 0:
                flag = False
                break
            if po == n:
                flag = True
                break
            if po > n:
                flag = False
                break
        
        return flag