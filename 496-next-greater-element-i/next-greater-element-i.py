class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = len(nums2)
        res = [-1]*k
        stack = []
        ele_to_nge = dict()
        for i in range(k-1, -1, -1):
            while(stack and stack[-1] <= nums2[i]):
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums2[i])
        
        for i in range(k):
            ele_to_nge[nums2[i]] = res[i]

        return [ele_to_nge[ele] for ele in nums1]