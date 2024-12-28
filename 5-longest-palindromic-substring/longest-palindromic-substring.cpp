class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if(n <= 1)   return s; 
        string res = "";
        string temp = "";
        for(int i=1; i < n; i++){
            // string odd = odd_pali(s, i);

            temp = temp+string(1,s[i]);
            int j = 1;
            while(i-j >= 0 && i+j < n && s[i-j] == s[i+j]){
                temp = s.substr(i-j, 2*j+1);
                j++;
            }
            if(temp.size() > res.size())    res = temp;
            temp = "";

            j = 0;
            while(i-1-j >= 0 && i+j < n && s[i-1-j] == s[i+j]){
                temp = s.substr(i-1-j,2*(j+1));
                j++;
            }
            if(temp.size() > res.size())    res = temp;
            temp = "";
        }        
        // if(res =="")    return string(1,s[0]);
        return res;
    }
};