class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack = []
        n = len(heights)

        def nse(arr):
            stack = []
            nse_arr = [n]*n
            for i in range(n-1, -1, -1):
                while(stack and arr[stack[-1]] >= arr[i]):
                    stack.pop()
                
                if stack:
                    nse_arr[i] = stack[-1]
                stack.append(i)
            return nse_arr

        
        def pse(arr):
            stack = []
            pse_arr = [-1]*n
            for i in range(n):
                while(stack and arr[stack[-1]] >= arr[i]):
                    stack.pop()
                
                if stack:
                    pse_arr[i] = stack[-1]
                stack.append(i)
            return pse_arr
        
        nse_arr = nse(heights)
        pse_arr = pse(heights)

        res = 0
        for i in range(n):
            temp = (nse_arr[i]-pse_arr[i]-1)*heights[i]
            if temp > res:
                res = temp

        return res
