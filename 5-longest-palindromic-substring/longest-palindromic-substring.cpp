class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if(n <= 1)   return s; 
        string res = "";
        string temp = "";
        for(int i=1; i < n; i++){

            temp = temp+string(1,s[i]);
            int j = 1;
            while(i-j >= 0 && i+j < n && s[i-j] == s[i+j]){
                temp = s[i-j]+temp+s[i+j];
                j++;
            }
            if(temp.size() > res.size())    res = temp;
            temp = "";

            j = 0;
            while(i-1-j >= 0 && i+j < n && s[i-1-j] == s[i+j]){
                temp = s[i-1-j]+temp+s[i+j];
                j++;
            }
            if(temp.size() > res.size())    res = temp;
            temp = "";
        }        
        return res;
    }
};