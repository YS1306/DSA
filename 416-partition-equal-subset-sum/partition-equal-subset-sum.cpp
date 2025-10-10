#include<numeric>
class Solution {
public:

    bool func(int ind,int s1,int s2,vector<int> nums, vector<vector<vector<int>>>& dp){
        if (dp[ind][s1][s2] != -1)
            return dp[ind][s1][s2];
        if(ind == 0)
            return (min(s1,s2)+nums[0] == max(s1, s2));
        bool take_in_1 = func(ind-1, s1+nums[ind], s2, nums, dp);
        bool take_in_2 = func(ind-1, s1, s2+nums[ind], nums, dp);
        dp[ind][s1][s2] = (take_in_1 || take_in_2);
        return dp[ind][s1][s2];
    }

    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        int total = accumulate(nums.begin(), nums.end(), 0);
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