class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for i in range(n+1)]

        dp[n][0] = 0
        dp[n][1] = 0

        for i in range(n-1, -1, -1):
            if dp[i+1][0] > -prices[i]+dp[i+1][1]:
                dp[i][0] = dp[i+1][0]
            else:
                dp[i][0] = -prices[i]+dp[i+1][1]
            
            if dp[i+1][1] > prices[i]+dp[i+1][0]:
                dp[i][1] = dp[i+1][1]
            else:
                dp[i][1] = prices[i]+dp[i+1][0]

        return dp[i][0]  