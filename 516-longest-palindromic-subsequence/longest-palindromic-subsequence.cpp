class Solution {
public:
    int longestPalindromeSubseq(string s) {
        string s2 = s;
        // reverse(s2.begin(), s2.end());
        int n = s.length();
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));

        for(int i = 1; i <= n; ++i){
            for(int j = 1; j <= n; ++j){
                if(s[i-1] == s2[n-j])
                    dp[i][j] = 1+dp[i-1][j-1];
                else{
                    if(dp[i-1][j] > dp[i][j-1])
                        dp[i][j] = dp[i-1][j];
                    else
                        dp[i][j] = dp[i][j-1];
                }
            }
        }

        return dp[n][n];
    }
};