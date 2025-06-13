class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def check(nums, curr_list, curr_sum, target):
            print(len(nums), len(curr_list), curr_sum)
            print()
            if curr_sum > target:
                return
            if curr_sum == target:
                if curr_list not in res:
                    res.append(curr_list)
                return
            if len(nums) == 0:
                return 
            
            if curr_sum <= target-nums[0]:
                # if len(nums) > 1 and nums[0] == nums[1]:
                #     check(nums[2:], curr_list+[nums[0]], curr_sum+nums[0], target)
                # else:
                    check(nums[1:], curr_list+[nums[0]], curr_sum+nums[0], target)
                    
            
            # if curr_sum <= target and nums[0] == nums[-1]:
            #     return
            while(len(nums) > 1 and nums[0] == nums[1]):
                nums = nums[1:]
            if len(nums) > 1 and nums[0] == nums[1]:
                    check(nums[2:], curr_list, curr_sum, target)
            else:
                check(nums[1:], curr_list, curr_sum, target)


        if min(candidates) != max(candidates):
            candidates.sort()
        check(candidates, [], 0, target)  
        return res