class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n = len(nums2)
        for i in nums1:
            flag = False
            for j in range(len(nums2)):
                if not flag and i == nums2[j]:
                    flag = True
                elif flag and nums2[j] > i:
                    res.append(nums2[j])
                    break
                if flag and j == n-1:
                    res.append(-1)
                    break
            
        return res