class Solution:
    


    def generateParenthesis(self, n: int) -> List[str]:

        def valid(open, close):
            if open == 1 and close == 1:
                return ['()']
            if open < 1 and close == 1:
                return [')']
            res1 = []
            res2 = []
            if open > 0:
                res1 = valid(open-1, close)
                for i in range(len(res1)):
                    res1[i] = '('+ res1[i]
            if close > 0 and open < close:
                res2 = valid(open, close-1)
                for j in range(len(res2)):
                    res2[j] = ')'+res2[j]
                
            return res1+res2
            
        return valid(n,n)
