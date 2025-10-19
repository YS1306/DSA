class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Can be solved using the nge approach
        n = len(prices)
        i = 0
        profit = 0
        while(i < n-1):
            if prices[i] <= prices[i+1]:
                profit += prices[i+1]-prices[i]
            i += 1
        return profit