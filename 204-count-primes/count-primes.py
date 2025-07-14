
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1 for i in range(n+1)]
        res = 0
        for i in range(2,n):
            if primes[i] == 1:
                res += 1
                j = i*i
                while(j <= n):
                    primes[j] = 0
                    j = j+i
        # print(res)
        return res