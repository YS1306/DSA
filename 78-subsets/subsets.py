class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def check(i,curr):
            if curr not in res:
                res.append(curr)
            if i >=  n:
                return
            check(i+1, curr)
            check(i+1, curr+[nums[i]])
            return
        
        check(0, [])
        return res