class Solution:
    def trap(self, nums: List[int]) -> int:
        res = 0
        left = 0; right = len(nums)-1
        l_max = nums[0]; r_max = nums[-1]

        while(left < right):
            if nums[left] <= nums[right]:
                if l_max > nums[left]:
                    res += (l_max-nums[left])
                else:
                    l_max =  nums[left]
                left += 1
            else:
                if r_max > nums[right]:
                    res += (r_max-nums[right])
                else:
                    r_max =  nums[right]
                right -= 1
                
            
        return res
            