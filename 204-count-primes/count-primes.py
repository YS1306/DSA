
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
            i += 1

        return primes[2:].count(1)
        