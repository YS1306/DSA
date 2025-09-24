class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        curr = 1

        for i in range(n):
            temp = prev+curr
            prev = curr
            curr = temp
        
        return curr