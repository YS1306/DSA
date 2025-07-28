from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        q = deque()
        res = []
        for i in range(n):
            while(q and q[0] <= i-k):
                q.popleft()
            
            while(q and nums[q[-1]] <= nums[i]):
                q.pop()
            
            q.append(i)
            if i >= k-1:
                # print(q)
                res.append(nums[q[0]])

        return res

        # def nge(nums):
        #     nge_arr = [n]*n
        #     stack = []
        #     for i in range(n-1, -1, -1):
        #         while(stack and nums[stack[-1]] < nums[i]):
        #             stack.pop()
        #         if stack:
        #             nge_arr[i] = stack[-1]
        #         stack.append(i)
        #     return nge_arr                

        # def pge(nums):
        #     pge_arr = [-1]*n
        #     stack = []
        #     for i in range(n):
        #         while(stack and nums[stack[-1]] < nums[i]):
        #             stack.pop()
        #         if stack:
        #             pge_arr[i] = stack[-1]
        #         stack.append(i)
        #     return pge_arr
        
        # nge_arr = nge(nums)
        # pge_arr = pge(nums)
        # print(nge_arr)
        # print(pge_arr)
        # res = []
        # for i in range(n):
        #     if nge_arr[i]-pge_arr[i] > k:
        #         # if not k%2 and (min(nge_arr[i]-i, i-pge_arr[i]) == k-2 and max(nge_arr[i]-i, i-pge_arr[i]) == k-1):
        #         #     res += [nums[i]]*(min(nge_arr[i]-i, i-pge_arr[i])-1)
        #         if nge_arr[i]-i ==  i-pge_arr[i] == k-1:
        #             res += [nums[i]]*(nge_arr[i]-i-1)
        #         else:
        #             # res += [nums[i]]*min(nge_arr[i]-pge_arr[i]-k,min(nge_arr[i]-i, i-pge_arr[i]))
        #             res += [nums[i]]*min(nge_arr[i]-i, i-pge_arr[i])
        # print(res)
        return res
