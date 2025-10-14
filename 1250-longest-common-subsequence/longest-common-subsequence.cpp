class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size(), m = text2.size();
        
        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));

        for(int i = 1; i<=n; i++){
            for(int j = 1; j<=m; j++){
                int left = dp[i][j-1];
                int top = dp[i-1][j];
                int corner = dp[i-1][j-1];
                if((text1[i-1] == text2[j-1]))
                    dp[i][j] = 1 + corner;
                else if(left > top)
                    dp[i][j] = left;
                else
                    dp[i][j] = top;
            }
        }

        return dp[n][m];

    }
};