class Solution {
public:
    bool ispal(string temp){
        int n = temp.size();
        for(int i=0; i <= n/2; i++){
            if(temp[i] != temp[n-i-1])  return false;
        }
        return true;
    }

    string check(string s, string rev){
        int i = 0;
        int n = s.size();
        string res = "";
        while(i<n && n-i > res.size()/2){
            int j = 0;
            while(j < n-i){
                if(s[i] == rev[j]){
                    int k = 0;
                    int next = 0;
                    string temp = "";
                    int flag = true;
                    while(i+k < n && j+k < n && s[i+k] == rev[j+k]){
                        temp.push_back(s[i+k]);
                        k++;
                        if(rev[j+k] == s[i]){    next = j+k;  }
                    }
                    if(temp.size() > res.size() and ispal(temp))    res = temp;
                    if(next)    j=next;
                    else j = j+k;
                }
                else j++;
            }
            i++;
        }    
        return res;    
    }

    string longestPalindrome(string s) {
        
        string rev = s;
        reverse(rev.begin(), rev.end());
        string front = check(s, rev);
        string back = check(rev, s);

        return max(front, back);
    }
};