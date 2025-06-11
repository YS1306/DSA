class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def check(nums,curr_list, curr_sum, target):

            if curr_sum > target:
                return 
            if curr_sum == target:
                res.append(curr_list)
                return
            if len(nums) == 0:
                return 
            if curr_sum <= target-nums[0]:
                take = check(nums, curr_list+[nums[0]], curr_sum+nums[0], target)
            no_take = check(nums[1:],curr_list, curr_sum, target)

            return 

        check(candidates, [],0, target)
        return res