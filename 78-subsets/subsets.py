class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) ==1:
            return [[],[nums[0]]]
        
        res = self.subsets(nums[1:])
        curr = []
        # print(res)
        for i in range(len(res)):
            new = res[i]+[nums[0]]
            if new not in res:
                curr.append(new)
        
        return res+curr