class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        maxi = prices[-1]
        for i in range(n-2, -1, -1):
            if prices[i] > maxi:
                maxi = prices[i]
            if maxi-prices[i] > res:
                res = maxi-prices[i]
            
        return res
        
            