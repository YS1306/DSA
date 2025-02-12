class Solution {
public:
    
    int maximumSum(vector<int>& nums) {
        int res = -1;
        map<int, int> sums; 
        for(int i=0; i<nums.size(); i++){
            int num = nums[i];
            int sum = 0;
            while(num > 0){
                sum += num%10;
                num = num/10;
            }
            if(sums.find(sum) != sums.end()){
                if(sums[sum]+nums[i] > res){
                    res = sums[sum]+nums[i];
                }
                if(nums[i] > sums[sum]){
                    sums[sum] = nums[i];
                }
            }
            else{
                sums[sum] = nums[i];
            }
        }
        return res;
        
    }
};