class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = max(nums[0], 0)
        if n > 1:
            dp[1] = max(0, nums[0], nums[1])
        else:
            return dp[0]
        
        for i in range(2, n):
            take, no_take = 0,0
            take = dp[i-2] + nums[i]
            no_take = dp[i-1]

            dp[i] = max(take, no_take)

        return dp[n-1]