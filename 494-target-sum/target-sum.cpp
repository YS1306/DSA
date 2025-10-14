#include<numeric>
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int total = 0;
        for(auto it:nums)
            total += abs(it);
        total = abs(total);
        if(target < 0)
            target *= -1;
        if(target > total || target < -1*total)
            return 0;
        
        if(target == 0 && total == 0){
            return 1<<n;
        }

        vector<unordered_map<int, int>> dp(n);
        for(int i = 0; i<n; i++){
            dp[i][nums[i]] += 1;
            dp[i][(-1)*nums[i]] += 1;
        }

        
        for(int i = 1; i<n; i++){
            for(int j = -1*total+1; j<=total ; j++){
                int plus =0, minus = 0;
                if(j-nums[i] <= total && j-nums[i] >= -1*total){
                    plus = dp[i-1][j-nums[i]];
                    minus = dp[i-1][j+nums[i]];
                }
                dp[i][j] = plus+minus; 
            }
        } 
    
        return dp[n-1][target];
        
    }
};