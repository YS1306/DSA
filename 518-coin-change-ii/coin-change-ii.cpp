class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int n = coins.size();

        vector<vector<long long>> dp(n, vector<long long>(amount+1, 0));

        for(int i=0; i<n; i++){
            dp[i][0] = 1;
            
        }
        if(coins[0] <= amount)
            dp[0][coins[0]] = 1; 
        
        for(int i=0; i < n; i++){
            for(int j=1; j<= amount; j++){
                
                int not_take = 0;
                if(i > 0)
                    not_take = dp[i-1][j];
                int repeat = 0;
                int no_repeat = 0;
                if(j >= coins[i]){
                    repeat = dp[i][j-coins[i]];
                }
                // if(dp[i][j] < not_take+repeat+no_repeat)
                dp[i][j] = not_take + (long long)repeat;
            }
        }

        return dp[n-1][amount];
        
    }
};