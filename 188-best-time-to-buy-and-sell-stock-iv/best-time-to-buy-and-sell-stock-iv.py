class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*(k+1) for j in range(2)] for i in range(n+1) ]
        print()
        for i in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy:
                        if -prices[i]+dp[i+1][0][cap] > dp[i+1][1][cap]:
                            dp[i][buy][cap] = -prices[i]+dp[i+1][0][cap]
                        else:
                            dp[i][buy][cap] = dp[i+1][1][cap]
                    else:
                        if prices[i]+dp[i+1][1][cap-1] > dp[i+1][0][cap]:
                            dp[i][buy][cap] = prices[i]+dp[i+1][1][cap-1]
                        else:
                            dp[i][buy][cap] = dp[i+1][0][cap]
        return dp[0][1][k]