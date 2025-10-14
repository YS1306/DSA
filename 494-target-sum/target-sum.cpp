#include<numeric>
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
    
        int n = nums.size();
        int total = 0;
        for(auto it:nums)
            total += it;
        // if(target < 0)
        //     target *= -1;
        if(target > total || (total-target)%2 != 0)
            return 0;
        if(target == 0 && total == 0){
            return 1<<n;
        }
        

        int D = (total-target)/2;

        vector<vector<int>> dp(n, vector<int>(D+1, 0));
        
        dp[0][0] = 1;
        if(nums[0] <= D){
            dp[0][nums[0]] = 1;
            if(nums[0] == 0)
                dp[0][0] = 2;
        }
        
        for(int i = 1; i<n; i++){
            for(int j = 0; j<=D ; j++){
                int plus =0, minus = 0;
                if(nums[i] <= j){
                    plus = dp[i-1][j-nums[i]];
                    
                }
                minus = dp[i-1][j];
                dp[i][j] = plus+minus; 
            }
        } 
    
        return dp[n-1][D];
        
    }
};