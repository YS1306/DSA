class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m , vector<int>(n, 0));
        int right = 0, down = 0;
        int big = max(m,n);
        for(int i=0; i<big; i++){
            if(i<n)
                dp[m-1][i] = 1;
            if(i < m)
                dp[i][n-1] = 1;
        }
        for(int i=m-2; i>=0; i--){
            for(int j=n-2; j >= 0; j--){
                right = dp[i][j+1];
                down = dp[i+1][j];
                dp[i][j] = right+down;
            }
        }
        

        return dp[0][0];
        
    }
};