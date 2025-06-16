class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def check(nums, curr_list, curr_sum):
            if len(curr_list) == k:
                if curr_sum == n and curr_list not in res:
                    res.append(curr_list)
                return
            
            if len(nums) == 0:
                return 
            
            check(nums[1:], curr_list+[nums[0]], curr_sum+nums[0])
            check(nums[1:], curr_list, curr_sum)

        nums = [i for i in range(1,10)]
        check(nums, [], 0)
        return res