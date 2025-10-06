class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));

        // Store minimum sum between right and down

        dp[m-1][n-1] = grid[m-1][n-1];
        int big  = max(m,n);
        for(int i = big-2; i >= 0; i--){
            if(i < m-1)
                dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1];
            if(i < n-1)
                dp[m-1][i] = grid[m-1][i] + dp[m-1][i+1];
        }

        // for(int i = n-2; i >= 0; i--){
            
        // }

        for(int i=m-2; i>=0; i--){
            for(int j = n-2; j>=0; j--){
                dp[i][j] = min(
                    grid[i][j]+dp[i][j+1],
                    grid[i][j]+dp[i+1][j]
                );
            }
        }

        return dp[0][0];


    }
};