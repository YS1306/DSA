class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = []

        res = [-1]*n
        # max_i = 0

        # for i in range(n):
        #     if nums[i] >= nums[max_i]:
        #         max_i = i
        nums = nums.copy() + nums.copy()

        for i in range(2*n-1,-1,-1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st and i < n:
                res[i] = st[-1]
            st.append(nums[i])  

        # res = res[n-max_i-1:]+res[:n-max_i-1]
        return res