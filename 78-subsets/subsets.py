class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def check(nums,i,curr):
            if curr not in res:
                res.append(curr)
            if i >=  n:
                return
            check(nums[1:], i+1, curr)
            check(nums[1:], i+1, curr+[nums[0]])
            return
        
        check(nums, 0, [])
        return res