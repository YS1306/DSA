class Solution {
public:
    int minInsertions(string s) {
        int n = s.length();
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));

        for(int i = 1; i <= n; ++i){
            for(int j = 1; j <= n; ++j){
                if(s[i-1] == s[n-j])
                    dp[i][j] = 1+dp[i-1][j-1];
                else{
                    if(dp[i-1][j] > dp[i][j-1])
                        dp[i][j] = dp[i-1][j];
                    else
                        dp[i][j] = dp[i][j-1];
                }
            }
        }
        int res = 0;
        for(int i=1; i <= n; i++){
            if(dp[i][i] == dp[i-1][i-1])
                res += 1;
        }

        return res;
    }
};