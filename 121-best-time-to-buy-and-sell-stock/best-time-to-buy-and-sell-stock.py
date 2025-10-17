class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        st = []
        nge = [n for i in range(n)]
        for i in range(n-1, -1, -1):
            while st and prices[st[-1]] < prices[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            st.append(i)
        res = [0]*n
        maxi = 0
        for i in range(n-1, -1, -1):
            if(nge[i] == n):
                res[i] == 0
            else:
                res[i] = prices[nge[i]]-prices[i]+res[nge[i]]
                if res[i] > maxi:
                    maxi = res[i]
        return maxi
            