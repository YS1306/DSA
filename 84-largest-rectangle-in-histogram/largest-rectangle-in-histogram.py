class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)
        
        stack = []
        res = 0
        pse_arr = [-1]*n
        for i in range(n):
            while(stack and arr[stack[-1]] >= arr[i]):
                temp = stack.pop()
                res = max(res, (i-pse_arr[temp]-1)*arr[temp])

            if stack:
                pse_arr[i] = stack[-1]
            stack.append(i)
        
        while(stack):
            temp = stack.pop()
            res = max(res, (n-pse_arr[temp]-1)*arr[temp])

        return res