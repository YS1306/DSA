class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        int not_take = 100000;
        int repeat = 100000;
        int no_repeat = 100000;
        vector<vector<int>> dp(n, vector<int>(amount+1, 100000));
        for(int i = 0; i<n; i++){
            dp[i][0] = 0;
            if(coins[i] <= amount)
                dp[i][coins[i]] = 1;
        }
        // for(int j = 0; j<=amount; j+=coins[0])
        //     dp[0][j] = int(j/coins[0]);
        
        for(int i=0; i< n; i++){
            for(int j=1; j<= amount; j++){
                not_take = 100000;
                if(i > 0)
                    not_take = dp[i-1][j];
                repeat = 100000;
                no_repeat = 100000;
                if(j >= coins[i]){
                    repeat = 1+dp[i][j-coins[i]];
                    if(i > 0)
                    no_repeat = 1+dp[i-1][j-coins[i]];
                }
                if( not_take <= repeat && not_take <= no_repeat)
                    dp[i][j] = not_take;
                else if(no_repeat <= repeat && no_repeat <= not_take )
                    dp[i][j] = no_repeat;
                else
                    dp[i][j] = repeat;
            }
        }

        if(dp[n-1][amount] >= 100000)
            return -1;
        return dp[n-1][amount];
    }
};