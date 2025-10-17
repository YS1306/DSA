class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(m+1):
            dp[0][i] = i
        for i in range(n+1):
            dp[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                     dp[i][j] = dp[i-1][j-1]
                else:
                    insertion = 1 + dp[i-1][j]
                    deletion = 1 + dp[i][j-1]
                    replacement = 1 + dp[i-1][j-1]
                    if(insertion <= deletion and insertion <= replacement):
                        # print(insertion, deletion, replacement)
                        dp[i][j] = insertion
                        # print(dp[i][j])
                    elif(insertion >= deletion and deletion <= replacement):
                        dp[i][j] = deletion
                    else:
                        dp[i][j] = replacement

                
        # print(dp)
        return dp[n][m]