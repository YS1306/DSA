class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        # largest = 0
        # for i in range(n):
        #     curr = heights[i]
        #     if not stack or stack[-1][1] <= curr:
        #         stack.append((i,curr))
        #     elif stack and stack[-1][1] > curr:
        #         ar = 0
        #         cnt = 0
        #         while(stack and stack[-1][1] > curr):
        #             ar += min(ar, stack[-1])
        #             stack.pop()
        #             cnt += 1
        #         largest = max(ar, largest)
                
        #         if  stack:
        #             last = stack[-1]
        #             for j in range(cnt):
        #                 stack.push(min(curr, last))

        # print(max())

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
            res = max(res, heights[i]*(nse_arr[i]-pse_arr[i]-1))

        print(res)
        return res
