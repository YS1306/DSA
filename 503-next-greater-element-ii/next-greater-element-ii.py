class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []
        # st2 = []
        res = [-1]*n
        max_ele = max(nums)
        cnt = 0
        while(nums[-1] != max_ele):
            nums = [nums[-1]] + nums[:-1]
            cnt += 1

        for i in range(n-1,-1,-1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                res[i] = st[-1]
            st.append(nums[i])  
        
        for j in range(cnt):
            res = res[1:]+[res[0]]
        return res