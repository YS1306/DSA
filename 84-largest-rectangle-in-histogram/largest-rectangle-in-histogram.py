class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)
        
        stack = []
        res = 0
        pse_arr = [-1]*n
        for i in range(n):
            while(stack and arr[stack[-1]] >= arr[i]):
                temp = stack.pop()
                val = (i-pse_arr[temp]-1)*arr[temp]
                if res < val:
                    res = val

            if stack:
                pse_arr[i] = stack[-1]
            stack.append(i)
        
        while(stack):
            temp = stack.pop()
            val = (n-pse_arr[temp]-1)*arr[temp]
            if res < val:
                res = max(res,val )

        return res