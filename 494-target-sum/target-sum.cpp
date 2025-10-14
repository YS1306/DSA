#include<numeric>
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        int total = accumulate(nums.begin(), nums.end(), 0);
        // for(auto it:nums)
            // total += abs(it);
        
        if(target < 0)
            target *= -1;
        if(target > abs(total) || target < -1*abs(total))
            return 0;
        
        // if(target == abs(total) and target == -1*abs(total))
        //     return 2;
        // cout<<target<<"\t"<<total;
        if(target == 0 && total == 0){
            return pow(2, n);
        }

        vector<unordered_map<int, int>> dp(n);
        for(int i = 0; i<n; i++){
            for(int j=-1*abs(total); j<abs(total)+1; j++){
                dp[i][j] = 0;
            }
            dp[i][nums[i]] += 1;
            dp[i][(-1)*nums[i]] += 1;
        }

        
        for(int i = 1; i<n; i++){
            for(int j = -1*abs(total)+1; j<=abs(total) ; j++){
                int plus = dp[i-1][j-nums[i]];
                int minus = dp[i-1][j+nums[i]];

                dp[i][j] = plus+minus; 
            }
        } 
    
        return dp[n-1][target];
        
    }
};