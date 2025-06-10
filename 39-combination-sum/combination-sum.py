class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def check(nums, curr_sum, target):
            if sum(curr_sum) > target:
                return 
            if sum(curr_sum) == target:
                res.append(curr_sum)
                return
            if len(nums) == 0:
                return 
            

            take = check(nums, curr_sum+[(nums[0])], target)
            no_take = check(nums[1:], curr_sum, target)

            return 

        check(candidates, [], target)
        return res