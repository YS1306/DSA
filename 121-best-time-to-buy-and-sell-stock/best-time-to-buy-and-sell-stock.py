class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        st = []
        nge = [0 for i in range(n)]
        st.append(n-1)
        res = 0
        for i in range(n-2, -1, -1):
            while st and prices[st[-1]] <= prices[i]:
                st.pop()
            if st:
                nge[i] = prices[st[-1]] - prices[i] + nge[st[-1]]
                if nge[i] > res:
                    res = nge[i]
            else:
                nge[i] = 0
            st.append(i)
        return res
        
            