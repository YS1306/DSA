class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[False]*(m+1) for i in range(n+1)]

        dp[0][0] = True
        if m == 0:
            if n == 0:
                return True
            else:
                return False
        
        if p[0] == "*":
            for i in range(n+1):
                dp[i][0] = True
                dp[i][1] = True
        for j in range(1,m+1):
            if(p[j-1] == "*"):
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = False

        for i in range(1,n+1):
            for j in range(1, m+1):
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[j-1] == '?':
                        dp[i][j] = dp[i-1][j-1]
                    elif p[j-1] == "*":
                        dp[i][j] = dp[i][j-1] or dp[i-1][j]
                    else:
                        dp[i][j] = False
        

        # print(dp)
        return dp[n][m]