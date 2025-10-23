class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]

        for i in range(n):
            for j in range(i):
                inc = 0
                if nums[i] > nums[j]:
                    inc = 1+dp[j]
                d_inc = dp[i]
                dp[i] = max(inc, d_inc)
        return max(dp)