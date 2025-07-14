
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1 for i in range(n)]
        res = 0
        i = 2
        while i < n:
            if primes[i] == 1:
                res += 1
                if i*i >= n:
                    i += 1
                    continue 
                j = i*i
                while(j < n):
                    primes[j] = 0
                    j = j+i
            i += 1

        return res
        