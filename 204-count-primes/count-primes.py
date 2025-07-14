
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1 for i in range(n+1)]
        res = []
        for i in range(2,n):
            if primes[i] == 1:
                res.append(i)
                j = i*i
                while(j <= n):
                    primes[j] = 0
                    j = j+i
        # print(res)
        return len(res)