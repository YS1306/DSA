class Solution {
public:
    string odd_pali(string s, int i){
        int n = s.length();
        string temp = "";
        temp = temp+string(1,s[i]);
        int j = 1;
        while(i-j >= 0 && i+j < n && s[i-j] == s[i+j]){
            temp = string(1,s[i-j])+temp+string(1,s[i+j]);
            j++;
        }
        return temp;
    }

    string even_pali(string s, int i){
        int n = s.length();
        bool left;
        string temp = "";
        if(i-1 >=0 && s[i-1] == s[i]){  left = true;   temp += string(1,s[i-1])+string(1,s[i]);     }
        else if(i+1 <n && s[i] == s[i+1]){ left = false;  temp += string(1,s[i])+string(1,s[i+1]);     }
        else return temp;
        if(left){
            int j = 1;

            while(i-1-j >= 0 && i+j < n && s[i-1-j] == s[i+j]){
                temp = string(1,s[i-1-j]) + temp + string(1,s[i+j]);
                j++;
            }
            return temp;
        }
        else{
            int j = 1;
            while(i-j >= 0 && i+1+j < n && s[i-j] == s[i+1+j]){

                temp = string(1,s[i-j]) + temp + string(1,s[i+1+j]);
                j++;
            }
            return temp;
        }
    }

    string longestPalindrome(string s) {
        int n = s.size();
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
            string odd = temp;
            temp = "";

            // string even = even_pali(s, i);
            j = 0;
            while(i-1-j >= 0 && i+j < n && s[i-1-j] == s[i+j]){
                temp = s.substr(i-1-j,2*(j+1));
                j++;
            }
            cout<<odd<<'\t'<<temp<<endl;
            if(temp.size() > odd.size())    odd = temp;

            if(odd.size() > res.size())  res = odd;
            temp = "";
        }        
        if(res =="")    return string(1,s[0]);
        return res;
    }
};