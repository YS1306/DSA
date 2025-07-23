class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 1000000007
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
                while(stack and arr[stack[-1]] > arr[i]):
                    stack.pop()
                
                if stack:
                    pse_arr[i] = stack[-1]
                stack.append(i)
            return pse_arr

        nse_arr = nse(arr)
        pse_arr = pse(arr)

        res = 0
        for i in range(n):
            res += (nse_arr[i]-i)*(i-pse_arr[i])*arr[i]        
        return res%mod