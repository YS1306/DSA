class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []
        # st2 = []
        res = [-1]*n
        max_i = 0

        for i in range(n):
            if nums[i] >= nums[max_i]:
                max_i = i
        nums = nums[max_i+1:] + nums[:max_i+1]
        # while(nums[-1] != max_ele):
        #     nums = [nums[-1]] + nums[:-1]
        #     cnt += 1

        for i in range(n-1,-1,-1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                res[i] = st[-1]
            st.append(nums[i])  

        res = res[n-max_i-1:]+res[:n-max_i-1]
        return res