class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> dp;
        int left = 0, right=0;
        for(int i=1; i<=n; i++){
            dp.push_back(vector<int>(i, 0));
        }

        for(int i=0; i<n; i++){
            dp[n-1][i] = triangle[n-1][i];
        }

        for(int i=n-2; i>=0; i--){
            for(int j=i;j>= 0; j-- ){
                left = triangle[i][j]+dp[i+1][j];
                right = triangle[i][j] + dp[i+1][j+1];
                if( left < right)
                    dp[i][j] = left;
                else
                    dp[i][j] = right;
            }
        }

        return dp[0][0];
    }
};