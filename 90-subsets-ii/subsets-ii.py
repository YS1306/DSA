class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def check(nums, curr_list):
            # print(curr_list)
            if len(nums) == 0:
                if curr_list not in res:
                    res.append(curr_list)
                return 
            if curr_list not in res:
                res.append(curr_list)


            check(nums[1:], curr_list+[nums[0]])
            while(len(nums)>1 and  nums[0] == nums[1]):
                # print("YES")
                nums = nums[1:]
            # if len(nums)>1 and  nums[0] == nums[1]:
            #     check(nums[2:], curr_list)
            # else:
            check(nums[1:], curr_list)
        if min(nums) != max(nums):
            nums = sorted(nums)
        check(nums, [])
        return res