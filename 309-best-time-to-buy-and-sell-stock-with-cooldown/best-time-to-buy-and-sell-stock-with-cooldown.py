class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for i in range(n+1)]

        for i in range(n-1, -1, -1):
            for buy in range(2):
                if buy:
                    dp[i][buy] = max(
                        -prices[i] + dp[i+1][0],
                        dp[i+1][1]
                    )
                else:
                    if i < n-1:
                        dp[i][buy] = max(
                            prices[i] + dp[i+2][1],
                            dp[i+1][0]
                        )
                    else:
                        dp[i][buy] = max(
                            prices[i],
                            dp[i+1][0]
                        )
        return dp[0][1]
