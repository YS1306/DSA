class Solution {
public:
    
    int maximumSum(vector<int>& nums) {
        int res = -1, num=0, sum =0;
        map<int, int> sums; 
        for(int i=0; i<nums.size(); i++){
            num = nums[i];
            sum = 0;
            while(num > 0){
                sum += num%10;
                num = num/10;
            }
            num = nums[i];
            if(sums.find(sum) != sums.end()){
                int add = sums[sum];
                res = max(res,add+num);
                sums[sum] = max(add,num);
            }
            else{
                sums[sum] = num;
            }
        }
        return res;
        
    }
};