class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        def nse(nums):
            nse_arr = [n]*n
            stack = []
            for i in range(n-1, -1, -1):
                while(stack and nums[stack[-1]] > nums[i]):
                    stack.pop()
                if stack:
                    nse_arr[i] = stack[-1]
                stack.append(i)
            return nse_arr                

        def pse(nums):
            pse_arr = [-1]*n
            stack = []
            for i in range(n):
                while(stack and nums[stack[-1]] >= nums[i]):
                    stack.pop()
                if stack:
                    pse_arr[i] = stack[-1]
                stack.append(i)
            return pse_arr

        def nge(nums):
            nge_arr = [n]*n
            stack = []
            for i in range(n-1, -1, -1):
                while(stack and nums[stack[-1]] < nums[i]):
                    stack.pop()
                if stack:
                    nge_arr[i] = stack[-1]
                stack.append(i)
            return nge_arr                

        def pge(nums):
            pge_arr = [-1]*n
            stack = []
            for i in range(n):
                while(stack and nums[stack[-1]] <= nums[i]):
                    stack.pop()
                if stack:
                    pge_arr[i] = stack[-1]
                stack.append(i)
            return pge_arr

        mins = 0

        nse_arr = nse(nums)
        pse_arr = pse(nums)
        nge_arr = nge(nums)
        pge_arr = pge(nums)

        for i in range(n):
            mins += ((nge_arr[i]-i)*(i-pge_arr[i])-(nse_arr[i]-i)*(i-pse_arr[i]))*nums[i]
            # maxs += *nums[i]
        
        return mins
