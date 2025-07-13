
class Solution:
    from sys import maxsize
    from math import sqrt
    def divide(self, dividend: int, divisor: int) -> int:
        maxi = int(sqrt((maxsize+1)>>1)-1)
        cnt = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
            
        else:
            sign = +1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        

        while(dividend >= divisor):
            i = 0
            while True:
                temp = divisor << (i+1)
                if temp > dividend:
                    break
                i += 1
            
            temp = 1<<i

            dividend = dividend-(divisor<<i)
            cnt += temp
            if dividend < divisor:
                break
        print(maxi)    
        if sign == -1:
            return (max((-maxi-1), cnt*sign))
        else:
            return min(maxi, cnt)
        
        return cnt*sign
        return cnt