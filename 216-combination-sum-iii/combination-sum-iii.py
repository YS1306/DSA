class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def check(nums, curr_list, target):
        
            if len(curr_list) == k:
                if target == 0:
                    res.append(curr_list)
                return
            
            if len(nums) == 0:
                return 
            
            check(nums[1:], curr_list+[nums[0]], target-nums[0])
            check(nums[1:], curr_list, target)


        nums = [i for i in range(1,min(10,n))]
        check(nums, [],  n)
        return res