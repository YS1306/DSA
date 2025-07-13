class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        temp = start^goal
        cnt = 0
        print(temp)
        while(temp > 0):
            b = temp&1
            
            cnt += b
            temp >>= 1
            # print(temp)
            # break
        return cnt