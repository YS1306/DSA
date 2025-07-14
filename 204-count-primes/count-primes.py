
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        i = 2
        while i*i < n:
            # if primes[i]:
            #     j = i*i
            #     while(j < n):
            #         primes[j] = False
            #         j += i
            primes[i*i:n:i] = [False] *((n-1-i*i)// i+1)
            if i == 2:
                i += 1
            else:
                i += 2

        return sum(primes)
        