class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k = len(nums1)
        res = [-1]*k
        
        n = len(nums2)
        for i in range(k):
            flag = False
            for j in range(nums2.index(nums1[i]), n):
                if not flag and nums1[i] == nums2[j]:
                    flag = True
                elif flag and nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
            
        return res