class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        ## No need to calculate PSE and NSE separately, instead we loop through the array only once and while popping any element the curr element will be NSE for it. So we just compare the res with (curr_idx-pse_arr[popping_idx]-1)*popping_element
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
                res = val

        return res