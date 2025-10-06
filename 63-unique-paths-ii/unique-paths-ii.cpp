class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<long>> dp(m , vector<long>(n, 0));
        long int right = 0, down = 0;
        int big = max(m,n);
        bool flag = false;
        if(obstacleGrid[0][0] || obstacleGrid[m-1][n-1])
            return 0;


        for(int i=n-1; i>=0; i--){
            if(obstacleGrid[m-1][i])
                break;
            dp[m-1][i] = 1;
        }
        for(int i = m-1; i>= 0; i--){
            if(obstacleGrid[i][n-1])
                break;
            dp[i][n-1] = 1;
        }



        for(int i=m-2; i>=0; i--){
            for(int j=n-2; j >= 0; j--){
                if( obstacleGrid[i][j] == 1){
                    dp[i][j] = 0;
                    continue;
                }
                right = dp[i][j+1];
                down = dp[i+1][j];
                dp[i][j] = right+down;
            }
        }

        return dp[0][0];
    }
};

