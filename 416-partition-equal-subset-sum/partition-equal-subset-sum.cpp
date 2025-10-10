#include<numeric>
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        int total = 0;
        for(auto num:nums){
            total += num;
        }
        // int total = accumulate(nums.begin(), nums.end(), 0);
        if(total%2) 
            return false;
        int target = int(total/2);
        vector<vector<bool>> dp(n, vector<bool>(target+1, false));
        for(int i=0; i<n; i++){
            dp[i][0] = true;
        }
        if(nums[0] < target)
            dp[0][nums[0]] = true;

        for(int i = 1; i < n; i++){
            for(int j=1; j<=target; j++){
                bool take = false;
                if(j >= nums[i])
                    take = dp[i-1][j-nums[i]];
                bool not_take = dp[i-1][j];

                dp[i][j] = (take || not_take);
            }
        }


        return dp[n-1][target];
    }
};