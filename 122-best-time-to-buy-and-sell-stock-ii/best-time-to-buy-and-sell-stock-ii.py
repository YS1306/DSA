class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Can be solved using the nge approach
        n = len(prices)
        i = 0
        j = 1
        profit = 0
        while(j < n):
            if prices[i] <= prices[j]:
                profit += prices[j]-prices[i]
            i = j
            j = i+1
        return profit