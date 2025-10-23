class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        maxi = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc = 1+dp[j]
                    if dp[i] < inc:
                        dp[i] = inc
                    if dp[i] > maxi:
                        maxi = dp[i]
        return maxi