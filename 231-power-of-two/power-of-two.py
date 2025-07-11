class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag = False
        dig = 1
        while True:
             
            if n%dig != 0:
                flag = False
                break
            if dig == n:
                flag = True
                break
            if dig > n:
                flag = False
                break
            dig <<= 1
            # print(dig)
        return flag