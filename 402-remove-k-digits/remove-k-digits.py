class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # find the first zero
        # if k == pos_first_zero
            # then return (num%10**(n-pos-1))

        # Very simple concept: If I have something bigger than me to my left, then I should remove it because it will make my number smaller. If the left digit is smaller, then no issue but otherwise I should remove it.
        
        stack = ''
        n = len(num)
        if k >= n:
            return "0"
        if num[k] == "0":
            return str(int(num[k:]))

        for i in range(n):
            while(k and stack and stack[-1] > num[i]):
                stack = stack[:-1]
                k -= 1
                
            stack += num[i]
        
        if k > 0:
            stack = stack[:-k]
        # for i in range(k):
        #     num = num[:stack[i]]+num[stack[i]+1:]
        #
        # print(str(stack))
        if stack == "0":
            return "0"

        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        
        stack = stack[i:]
        return stack
