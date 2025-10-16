class Solution {
public:
    
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();

        vector<vector<int>> dp(n+1, vector<int>(m+1, 0));

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(s[i-1] == t[j-1]){
                    dp[i][j] = 1+dp[i-1][j-1];
                }
                else{
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        if(dp[n][m] != m)   return 0;
        vector<vector<long>> res(n+1, vector<long>(m+1, 1));
        
        for(int i=1; i<=n; ++i){
            for(int j = 1; j<=m; ++j){
                int left = 0; 
                int up = 0;
                if(s[i-1] == t[j-1]){
                    int corner = res[i-1][j-1];
                    if(dp[i-1][j] == dp[i][j])
                        left = res[i-1][j];
                    if(dp[i][j-1] == dp[i][j])
                        up = res[i][j-1];
                    res[i][j] = (long)corner+(long)left+(long)up;
                }
                else{
                    if(dp[i-1][j] == dp[i][j])
                        left = res[i-1][j];
                    if(dp[i][j-1] == dp[i][j])
                        up = res[i][j-1];
                    res[i][j] = (long)left+(long)up;
                }
                    
            }
        }
        return res[n][m];
    }
};