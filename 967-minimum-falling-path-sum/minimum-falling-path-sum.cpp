class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int left = 100000, center = 100000, right=100000;
        vector<int> dp(n,0);
        vector<int> prev(n,0);

        for(int i=0; i<n; i++){
            prev[i] = matrix[n-1][i];
            dp[i] = matrix[n-1][i];
        }
        
        for(int i=n-2; i>=0; i--){
            
            for(int j=0; j<n; j++){
                left = right = center = 100000;

                if(j>0)
                    left = matrix[i][j] + prev[j-1];
                center = matrix[i][j] + prev[j];
                if(j < n-1)
                    right = matrix[i][j] + prev[j+1];
                if(left <= center && left <= right)
                    dp[j] = left;
                else if(center <= left && center <= right)
                    dp[j] = center;
                else
                    dp[j] = right;
                
            }
            prev = vector<int>(dp.begin(), dp.end());
        }

        int min_c = 100000;
        for(int i=0; i<n; i++){
            if(dp[i] < min_c)
                min_c = dp[i];
        }
        return min_c;
    }
};