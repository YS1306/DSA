
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1 for i in range(n)]

        i = 2
        while i*i < n:
            if primes[i] == 1:
                j = i*i
                while(j < n):
                    primes[j] = 0
                    j = j+i
            if i == 2:
                i += 1
            else:
                i += 2

        return sum(primes[2:])
        